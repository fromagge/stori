from datetime import timezone, datetime

from rest_framework import serializers
from apps.loans.models import Contact


class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'state', 'country', 'zip']
		required_fields = ['first_name', 'prefix', 'phone']