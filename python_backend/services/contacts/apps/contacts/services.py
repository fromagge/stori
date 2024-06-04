import logging
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotFound

from apps.contacts.models import Contact


class ContactService:

	@staticmethod
	def get_contacts(user_id, contact_id=None):
		if contact_id:
			try:
				Contact.objects.get(user_id=user_id, id=contact_id)
			except Contact.DoesNotExist:
				raise NotFound({'details': 'The contact does not exist'})

		return Contact.objects.filter(user_id=user_id).all()

	@staticmethod
	@transaction.atomic
	def create_contact(user_id: str, **contact_details):
		new_contact = Contact.objects.create(
			user_id=user_id,
			**contact_details
		)

		new_contact.save()
		return new_contact

	@staticmethod
	@transaction.atomic
	def update_contact(user_id, contact_id, **new_details):
		contact = ContactService.get_contacts(user_id=user_id, contact_id=contact_id)
		if not contact:
			raise NotFound({'details': 'The contact does not exist'})

		Contact.objects.filter(user_id=user_id, id=contact_id).update(**new_details)

		return Contact.objects.get(user_id=user_id, id=contact_id)

	@staticmethod
	@transaction.atomic
	def delete_contact(user_id, contact_id):
		contact = ContactService.get_contacts(user_id=user_id, contact_id=contact_id)
		if not contact:
			raise NotFound({'details': 'The contact does not exist'})

		try:
			contact.delete()
		except Exception as e:
			logging.error(e)
			raise ValidationError({'details': 'An error occurred while deleting the contact'})

		return True
