from concurrent import futures
import grpc
import logging

from services.auth import routes, service_pb2_grpc


def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

	# This could be in another file  ¯\_(ツ)_/¯

	service_pb2_grpc.add_AuthenticationServerServicer_to_server(routes.AuthServices(), server)

	logging.info("Server stating in Port 50051...")
	server.add_insecure_port('[::]:50051')
	server.start()
	server.wait_for_termination()


if __name__ == '__main__':
	serve()
