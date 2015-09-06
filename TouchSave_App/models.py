from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
# Create your models here.

class XUser(User):
    date_of_birth = models.DateField("Date of Birth")
    blood_type = models.CharField(max_length=5)
    default_date = models.BooleanField(True)
	
    def change_date(Date):
		date_of_birth = Date
		default_date = False
	
    def __str__(self):
       return self.first_name + self.last_name

    def close(self):
       self.is_active = False
       self.save()

class Allergies(models.Model):
    allergy = models.CharField(max_length=200)
    user_with_allergy = models.ForeignKey(XUser)

    def __str__(self):
        return str(self.allergy)

class Comments(models.Model):
    comment = models.CharField(max_length=500)
    users_commen = models.ForeignKey(XUser)

    def _str__(self):
       return str(self.comment)



