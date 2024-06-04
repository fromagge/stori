from django.http import JsonResponse

from apps.grpc_client import GrpcClient

class AuthMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		self.grpc_client = GrpcClient("your_server_address")

	def __call__(self, request):
		from apps.auth_pb2 import VerifyRequest

		token = request.headers.get('Authorization')

		if not token:
			return JsonResponse({'error': "You are unathorized"}, status=403)

		try:
			request.user_id = 1
			return self.get_response(request)
			response = self.grpc_client.verify(verify_request)
			print(response)
			if response.valid:
				request.user_id = response.user_id
				return self.get_response(request)
			else:
				return JsonResponse({'error': "You are unathorized"}, status=403)
		except Exception as e:
			return JsonResponse({'error': "You are unathorized"}, status=403)
