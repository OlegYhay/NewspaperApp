from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserUpdatedForm
from .models import Users


class UserChange(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserUpdatedForm
    list_display = ['email', 'username', 'age']
    model = Users


admin.site.register(Users, UserChange)
