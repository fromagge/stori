from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from models.base import Base


class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String, unique=True, nullable=False)
	password_hash = Column(String, nullable=False)
	create_date = Column(DateTime, default=datetime.utcnow)
	update_date = Column(DateTime, onupdate=datetime.utcnow)

	def save(self, commit=False):
		from models import session

		session.add(self)
		if commit:
			session.commit()
		return self
