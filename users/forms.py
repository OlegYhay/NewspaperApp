from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Users


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Users
        fields = ('username', 'email')


class CustomUserUpdatedForm(UserChangeForm):
    class Meta:
        models = Users
        fields = UserChangeForm.Meta.fields
