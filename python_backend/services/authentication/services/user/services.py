import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import Conflict

from models import session
from utils import is_password_strong, generate_tokens


class UserService:

	@staticmethod
	def get_user_by_username(username: str, raise_on_error=True) -> dict:
		from models import User

		user = session.query(User).filter(User.username == username).first()
		if not user:
			if raise_on_error:
				raise Conflict('User not found')
			else:
				return None

		return user

	@staticmethod
	def create_user(username: str, pwd: str) -> dict:
		from models import User

		existing_user = UserService.get_user_by_username(username, raise_on_error=False)
		if existing_user:
			raise Conflict('User already exists')

		password_strength = is_password_strong(pwd)
		if not password_strength:
			raise Conflict('Password is not strong enough, at least 8 characters and an uppercase letter is required')

		hashed_pwd = generate_password_hash(pwd)

		user = User(username=username, password_hash=hashed_pwd)
		user.save(commit=True)

		return user.id

	@staticmethod
	def check_user_password(password: str, password_hash: str) -> bool:
		return check_password_hash(password_hash, password)

	@staticmethod
	def generate_user_tokens(user_id: str) -> tuple:
		return generate_tokens(user_id)
