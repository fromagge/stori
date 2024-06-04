from datetime import timezone, datetime

from rest_framework import serializers
from apps.contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
	fields_to_remove = ['last_name', 'email', 'city', 'state', 'country', 'zip']

	class Meta:
		model = Contact
		fields = ['id','first_name', 'last_name', 'email', 'prefix','phone', 'city', 'state', 'country', 'zip']
		required_fields = ['first_name', 'prefix', 'phone']


	def to_representation(self, instance):
		data = super().to_representation(instance)
		for field in self.fields_to_remove:
			if data[field] is None:
				data.pop(field)
		return data

class ContactUpdateSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(required=False)
	last_name = serializers.CharField(required=False)
	email = serializers.EmailField(required=False)
	prefix = serializers.CharField(required=False)
	phone = serializers.CharField(required=False)
	city = serializers.CharField(required=False)
	state = serializers.CharField(required=False)
	country = serializers.CharField(required=False)
	zip = serializers.CharField(required=False)

	class Meta:
		model = Contact
		fields = ['first_name', 'last_name', 'email', 'prefix','phone', 'city', 'state', 'country', 'zip']
