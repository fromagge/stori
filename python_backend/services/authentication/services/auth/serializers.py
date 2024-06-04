from flask_marshmallow import Schema
from marshmallow import fields, EXCLUDE

class TokenSerializer(Schema):
	class Meta:
		unknown = EXCLUDE

	token = fields.String(required=True, allow_none=False)
