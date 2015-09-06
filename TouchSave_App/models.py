from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
# Create your models here.

class XUser(User):
    date_of_birth = models.DateField("Date of Birth")
    blood_type = models.CharField(max_length=5)
	allergies = models.CharField(max_length=500)
	comments = models.CharField(max_lengt=500)
    def __str__(self):
       return self.first_name + self.last_name

    def close(self):
       self.is_active = False
       self.save()


