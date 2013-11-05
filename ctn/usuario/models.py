from django.contrib.auth.models import User
from django.db import models

class CustomUser(models.Manager):
	username   = CharField(max_length=50)
	last_login = DateTimeField(blank=True)
	is_active  = BooleanField()
	is_authenticated():
	create_user():

