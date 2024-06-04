from django.db import models


class User(models.Model):
	class Meta:
		managed = False
		db_table = 'users'


class Contact(models.Model):
	__tablename__ = 'contacts'

	user_id = models.IntegerField()
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	prefix = models.CharField(max_length=10)
	phone = models.CharField(max_length=15)
	address = models.TextField(blank=True, null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	state = models.CharField(max_length=50, blank=True, null=True)
	country = models.CharField(max_length=50, blank=True, null=True)
	zip = models.CharField(max_length=10, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		indexes = [
			models.Index(fields=['user_id', 'id'])
		]
