from flask_marshmallow import Schema
from marshmallow import fields, EXCLUDE


class UserSerializer(Schema):
	class Meta:
		unknown = EXCLUDE

	username = fields.String(required=True)
	password = fields.String(required=True)
