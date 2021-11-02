from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from school.school_management_app.models import CustomerUser


class Usermodel(UserAdmin):
    pass;

admin.site.register(CustomerUser, Usermodel)