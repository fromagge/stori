from django.urls import path, include

urlpatterns = [
	path('contacts/', include('apps.contacts.urls')),
]
