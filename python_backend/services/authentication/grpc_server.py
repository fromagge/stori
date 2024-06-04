import os
from concurrent import futures
import grpc
import logging

logging.basicConfig(level=logging.DEBUG)

from services.auth import routes, service_pb2_grpc


def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

	# This could be in another file  ¯\_(ツ)_/¯

	service_pb2_grpc.add_AuthenticationServerServicer_to_server(routes.AuthServicesgRPC(), server)

	if not (PORT := os.environ.get('PORT')):
		PORT = 50051

	logging.info(f"Server stating in Port {PORT}...")
	server.add_insecure_port(f'[::]:{PORT}')
	server.start()
	server.wait_for_termination()


if __name__ == '__main__':
	serve()
