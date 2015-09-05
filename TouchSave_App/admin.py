from django.contrib import admin

# Register your models here.
from .models import XUser, Allergies, Comments
admin.site.register(XUser)
admin.site.register(Allergies)
admin.site.register(Comments)
