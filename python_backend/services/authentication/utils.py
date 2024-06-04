import logging
import jwt
import os
from functools import wraps
from datetime import datetime, timedelta

from flask import request
from werkzeug.exceptions import BadRequest

from grpc import StatusCode
from google.protobuf.json_format import MessageToDict

import marshmallow.exceptions
import authentication.clients.cache as cache


def is_password_strong(password: str) -> bool:
	"""
	Check if the password is strong enough. Really simple validation for now.
	"""
	return len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password)


def validate_grpc(pydantic_model):
	def decorator(func):
		@wraps(func)
		def wrapper(self, request, context):
			try:
				_dict = {}
				validated_request = pydantic_model()
			except Exception as e:
				context.set_code(StatusCode.INVALID_ARGUMENT)
				context.set_details(f'Invalid request: {str(e)}')
				return
			return func(self, validated_request, context)

		return wrapper

	return decorator


def validate_api(validation_schema):
	def decorator(func):
		def wrapper(*args, **kwargs):
			try:
				payload = validation_schema().load(request.get_json())
			except marshmallow.exceptions.ValidationError as e:
				raise BadRequest(description={'Invalid request': e.messages})

			return func(*args, payload=payload, **kwargs)

		return wrapper

	return decorator


def loggrpc(func):
	@wraps(func)
	def wrapper(self, request, context):
		logging.info(f'{func.__name__} request received')
		return func(self, request, context)

	return wrapper


def _generate_access_token(user_id: str) -> str:
	time_now = datetime.utcnow()
	secret_key = os.getenv('SECRET_KEY')
	token_expiration = os.getenv('TOKEN_EXPIRATION', 3600)

	payload = {
		'user_id': user_id,
		'exp': time_now + timedelta(seconds=token_expiration),
		'type': 'access'
	}

	return jwt.encode(payload, secret_key, algorithm='HS256')


def _generate_refresh_token(user_id: str) -> str:
	time_now = datetime.utcnow()
	secret_key = os.getenv('SECRET_KEY')
	refresh_token_expiration = os.getenv('REFRESH_TOKEN_EXPIRATION', 86400)

	payload = {
		'user_id': user_id,
		'exp': time_now + timedelta(seconds=refresh_token_expiration),
		'type': 'refresh'
	}

	return jwt.encode(payload, secret_key, algorithm='HS256')


def generate_tokens(user_id: str) -> tuple:
	access_token = _generate_access_token(user_id)
	refresh_token = _generate_refresh_token(user_id)

	cache.store_token(user_id, access_token)
	cache.store_refresh_token(user_id, refresh_token)

	return access_token, refresh_token
