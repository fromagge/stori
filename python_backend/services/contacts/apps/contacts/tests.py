from datetime import datetime, timedelta, timezone
from uuid import uuid4

from faker import Faker
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

from apps.contacts.models import Contact
from apps.contacts.services import ContactService


class ContactTestCase(TestCase):
	def setUp(self):
		Contact.objects.create(
			user_id=1,
			id=100,
			first_name='John',
			last_name='Doe'
		)

	def test_create_contact(self):

		# Let's create a contact and make sure it's active

		contact_details = {
			'first_name': 'John',
			'last_name': 'Doe',
			'email': 'johndoe@stori.com',
			'phone': '1234567890',
			'prefix': '+1',
			'city': 'Boston'
		}

		contact = ContactService.create_contact(user_id=1, **contact_details)
		contact = Contact.objects.get(user_id=1, id=contact.id)

		self.assertEqual(contact.first_name, 'John')
		self.assertEqual(contact.last_name, 'Doe')
		self.assertEqual(contact.email, 'johndoe@stori.com')
		self.assertEqual(contact.phone, '1234567890')

	def test_update_contact(self):
		new_contact_details = {
			'first_name': 'Pepe',
			'last_name': 'Grillo'
		}

		updated_contact = ContactService.update_contact(user_id=1, contact_id=100, **new_contact_details)

		self.assertEqual(updated_contact.first_name, 'Pepe')
		self.assertEqual(updated_contact.last_name, 'Grillo')

		contact = Contact.objects.get(user_id=1, id=100)

		self.assertEqual(contact.first_name, 'Pepe')
		self.assertEqual(contact.last_name, 'Grillo')

	def test_delete_contact(self):
		deleted = ContactService.delete_contact(user_id=1, contact_id=100)
		self.assertTrue(deleted)
		self.assertEqual(Contact.objects.filter(user_id=1, id=100).count(), 0)