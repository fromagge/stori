import logging
import os
from django.http import JsonResponse

from apps.grpc_client import GrpcClient


class AuthMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		server_address = os.environ.get('AUTH_SERVER_ADDRESS')
		self.grpc_client = GrpcClient(server_address)

	def __call__(self, request):
		from apps.auth_pb2 import VerifyRequest

		token = request.headers.get('Authorization')

		if not token:
			return JsonResponse({'error': "You are unathorized from the get got."}, status=403)

		try:
			response = self.grpc_client.verify_token(token)
			if response['valid']:
				request.user_id = response['userId']
				return self.get_response(request)
			else:
				return JsonResponse({'error': "Authorization invalid"}, status=403)
		except Exception as e:
			logging.error(f'Error: {e}')
			return JsonResponse({'error': "Something went wrong with you authorization"}, status=403)
