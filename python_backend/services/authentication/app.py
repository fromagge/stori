import os
from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from dotenv import load_dotenv

from services.auth.routes import AuthServicesLoginAPI, AuthServicesSignupAPI

load_dotenv()


def add_app_routes(app):
	api = Api(app)

	api.add_resource(AuthServicesLoginAPI, '/auth/login')
	api.add_resource(AuthServicesSignupAPI, '/auth/signup')


def create_app():
	app = Flask(__name__)
	CORS(app)
	add_app_routes(app)

	return app
