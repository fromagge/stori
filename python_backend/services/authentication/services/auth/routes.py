import logging
from flask_restx import Resource

import services.auth.service_pb2 as service_pb2
import services.auth.service_pb2_grpc as service_grpc
from services.auth.serializers import TokenSerializer
from services.user.services import UserService
from services.user.serializers import UserSerializer
from clients.token import JwtClient
from utils import validate_api, loggrpc, validate_grpc

logger = logging.getLogger(__name__)


class AuthServicesgRPC(service_grpc.AuthenticationServerServicer):

	@loggrpc
	@validate_grpc(TokenSerializer)
	def Verify(self, request, context):
		logger.info(f'Verify request received')
		claims = JwtClient.verify_token(request['token'])
		logger.info(f'Verify request processed')
		return service_pb2.VerifyResponse(message="Client is authenticated", valid=True, user_id=claims['user_id'])


class AuthServicesLoginAPI(Resource):

	@validate_api(UserSerializer)
	def post(self, payload):
		username = payload['username']
		user_found = UserService.get_user_by_username(username)

		if not user_found:
			return {'message': 'User not found'}, 404

		password = payload['password']

		is_valid = UserService.check_user_password(password, user_found.password_hash)
		if not is_valid:
			return {
				'message': 'Invalid password'}, 401

		token, refresh_token = UserService.generate_user_tokens(str(user_found.id))

		return {
			'user_id': user_found.id,
			'token': token,
			'refresh_token': refresh_token
		}, 200


class AuthServicesSignupAPI(Resource):

	@validate_api(UserSerializer)
	def post(self, payload):
		username = payload['username']
		user_found = UserService.get_user_by_username(username, raise_on_error=False)

		if user_found:
			return {'message': 'User already exists'}, 401

		new_user_id = UserService.create_user(username, payload['password'])

		return {'user_id': new_user_id}, 201
