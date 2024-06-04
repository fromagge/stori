from datetime import datetime, timedelta, timezone
from uuid import uuid4

from faker import Faker
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

from apps.contacts.models import User, Contact
from apps.contacts.services import ContactService


class ContactTestCase(TestCase):
	def setUp(self):
		User.objects.create(user_id=1)
		User.objects.create(user_id=2)

	def test_create_contact(self):
		user = User.objects.get(user_id=1)

		# Let's create a contact and make sure it's active

		contact_details = {
			'first_name': 'John',
			'last_name': 'Doe',
			'email': 'johndoe@stori.com',
			'phone': '1234567890',
			'prefix': '+1',
			'city': 'Boston'
		}

		contact = ContactService.create_contact(user_id=user.user_id, **contact_details)
		contact = Contact.objects.get(user_id=user.user_id, contact_id=contact.id)

		self.assertEqual(contact.first_name, 'John')
		self.assertEqual(contact.last_name, 'Doe')
		self.assertEqual(contact.email, 'johndoe@stori.com')
		self.assertEqual(contact.phone, '1234567890')
