from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# The default UserCreationForm did not include an 'Email' field, so I had to create a new form
class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user