from django import forms
from django.core import validators

class Loginform(forms.Form):
    name=forms.CharField(max_length=30,label="Enter your name")
    email=forms.EmailField(max_length=30,label="enter your email")
    text=forms.CharField(widget=forms.Textarea)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password=self.cleaned_data['password']
        if len(password)>5:
            raise forms.ValidationError("gvbhbbvd")
        return password