import grpc

from apps.auth_pb2 import VerifyRequest, VerifyResponse
from apps.auth_pb2_grpc import AuthenticationServerStub

from google.protobuf.json_format import MessageToDict


class GrpcClient:

	def __init__(self, server_address):
		self.channel = grpc.insecure_channel(server_address)

	def verify_token(self, token):
		stub = AuthenticationServerStub(self.channel)
		response = stub.Verify(VerifyRequest(token=token))
		return MessageToDict(**response)
