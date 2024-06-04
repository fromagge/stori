from flask_restx import Resource

import authentication.services.auth.service_pb2 as service_pb2
import authentication.services.auth.service_pb2_grpc as service_grpc
from authentication.services.user.serializers import UserSerializer
from authentication.services.user.services import UserService
from authentication.utils import validate_api, loggrpc, validate_grpc


class AuthServicesgRPC(service_grpc.AuthenticationServerServicer):

	@loggrpc
	@validate_grpc(UserSerializer)
	def Signup(self, request, context):
		username = request.username
		password = request.password

		new_user_id = UserService.create_user(username, password)

		return service_pb2.SignupResponse(user_id=new_user_id)

	def Login(self, request, context):
		pass

	def Verify(self, request, context):
		pass

	def Refresh(self, request, context):
		pass

	def Logout(self, request, context):
		pass

	def __init__(self):
		pass


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
