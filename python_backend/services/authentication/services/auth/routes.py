import services.auth.service_pb2 as service_pb2
import services.auth.service_pb2_grpc as service_grpc
from services.user.serializers import UserSerializer
from services.user.services import UserService
from utils import validate_request, loggrpc


class AuthServices(service_grpc.AuthenticationServerServicer):

	@loggrpc
	@validate_request(UserSerializer)
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
