from django.contrib import admin

from .models import Member, Award, Address 

# Register your models here.

admin.site.register(Member)

admin.site.register(Award)

admin.site.register(Address)

