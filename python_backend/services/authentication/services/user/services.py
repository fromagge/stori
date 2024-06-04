from werkzeug.security import generate_password_hash
from werkzeug.exceptions import Conflict

from utils import is_password_strong


class UserService:
	@staticmethod
	def create_user(username: str, pwd: str) -> dict:
		from models import User

		existing_user = User.query.filter_by(username=username).first()
		if existing_user:
			raise Conflict('User already exists')

		password_strength = is_password_strong(pwd)
		if not password_strength:
			raise Conflict('Password is not strong enough')

		hashed_pwd = generate_password_hash(pwd)

		user = User(username=username, password_hash=hashed_pwd)
		user.save(commit=True)

		return user.id
