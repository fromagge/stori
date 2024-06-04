from django.urls import path, include

from apps.contacts.views import ContactDetailView, ContactCreateView

urlpatterns = [
	path("", ContactCreateView.as_view(), name="create_contact"),
	path("<int:contact_id>", ContactDetailView.as_view(), name="get_contact"),
]
