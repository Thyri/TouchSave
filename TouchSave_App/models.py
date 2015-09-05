from django.db import models

# Create your models here.
Class Allergies(models.Model):
    allergy = models.CharField(maxlength=200)
    user_with_allergy = models.ForeignKey(XUser)

    def __str__(self):
        return str(self.allergy)

Class Comments(models.Model):
    comment = models.CharField(maxlength=500)
    users_commen = models.ForeignKey(XUser)

    def _str__(self):
       return str(self.comment)

Class XUser(User):
    date_of_birth = models.DateField("Date of Birth")
    first_name = models.CharField(maxlength=200)
    last_name = models.CharField(maxlength=200)
    blood_type = (
        ('0_neg', '0-'),
        ('0_pos', '0+'),
        ('A_neg', 'A-'),
        ('A_pos', 'A+'),
        ('B_neg', 'B-'),
        ('B_pos', 'B+'),
        ('AB_neg', 'AB-'),
        ('AB_pos', 'AB+'),
    )

    def __str__(self):
       return self.first_name + self.last_name

    def close(self):
       self.is_active = False
       self.save()


