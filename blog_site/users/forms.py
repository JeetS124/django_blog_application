from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile


class registerform(ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["name", "email", "password1", "password2"]

    def save(self):
        username = email = self.cleaned_data.get("email")
        name = self.cleaned_data.get("name")
        password1 = self.cleaned_data.get("password1")
        user = User.objects.create_user(
            username=username, email=email, password=password1, first_name=name
        )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["author", "profile_image"]
