from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common import validate
from apps.contacts.serializers import ContactSerializer, ContactUpdateSerializer

from apps.contacts.services import ContactService


class ContactCreateView(APIView):

	def get(self, request, *args, **kwargs):
		user_id = request.user_id
		contacts = ContactService.get_contacts(user_id)

		serialized_data = ContactSerializer(contacts, many=True)
		return Response(serialized_data.data, 200)

	@validate(ContactSerializer)
	def post(self, request, payload, *args, **kwargs):
		user_id = request.user_id
		contact = ContactService.create_contact(user_id, **payload)

		serialized_data = ContactSerializer(contact)
		return Response(serialized_data.data, 201)


class ContactDetailView(APIView):

	def get(self, request, contact_id, *args, **kwargs):
		user_id = request.user_id
		contact = ContactService.get_contacts(user_id, contact_id)

		serialized_data = ContactSerializer(contact.first())
		return Response(serialized_data.data, 200)

	@validate(ContactUpdateSerializer)
	def put(self, request,payload, contact_id, *args, **kwargs):
		user_id = request.user_id
		contact = ContactService.update_contact(user_id, contact_id, **payload)

		serialized_data = ContactSerializer(contact)
		return Response(serialized_data.data, 200)

	def delete(self, request, contact_id, *args, **kwargs):
		user_id = request.user_id
		is_deleted = ContactService.delete_contact(user_id, contact_id)
		if not is_deleted:
			return Response({}, 404)

		return Response({}, 204)
