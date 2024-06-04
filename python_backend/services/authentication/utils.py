
def is_password_strong(password: str) -> bool:
	"""
	Check if the password is strong enough. Really simple validation for now.
	"""
	return len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password)


from functools import wraps
from grpc import StatusCode
from google.protobuf.json_format import MessageToDict
import logging

def validate_request(pydantic_model):
	def decorator(func):
		@wraps(func)
		def wrapper(self, request, context):
			try:
				validated_request = pydantic_model(**MessageToDict(request))
			except Exception as e:
				context.set_code(StatusCode.INVALID_ARGUMENT)
				context.set_details(f'Invalid request: {str(e)}')
				return
			return func(self, validated_request, context)

		return wrapper

	return decorator

def loggrpc(func):
	@wraps(func)
	def wrapper(self, request, context):
		logging.info(f'{func.__name__} request received')
		return func(self, request, context)

	return wrapper