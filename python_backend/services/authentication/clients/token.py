import logging

import jwt
import os
from werkzeug.exceptions import Unauthorized

from clients import cache


class JwtClient:
	@staticmethod
	def verify_token(token: str) -> dict:
		secret_key = os.getenv('SECRET_KEY')

		claims = jwt.decode(token, options={"verify_signature": False})
		logging.error(claims)

		is_token_valid = cache.get_token(claims['user_id'])
		logging.error(is_token_valid)
		logging.error(token)
		if is_token_valid and is_token_valid is not None:
			if is_token_valid == token:
				return claims

		try:
			return jwt.decode(token, secret_key, algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			raise Unauthorized('Token has expired')
		except jwt.InvalidTokenError:
			raise Unauthorized('Invalid token')
		except Exception as e:
			raise Unauthorized('Something went wrong')
