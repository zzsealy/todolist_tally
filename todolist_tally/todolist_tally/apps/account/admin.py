from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from todolist_tally.apps.account.models import User

# Register your models here.


admin.site.register(User, UserAdmin)
from django.contrib import admin

# Register your models here.
