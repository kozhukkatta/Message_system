from django import forms
from .models import Login, Message

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=("__all__")
        widgets={
                'username':forms.TextInput(attrs={
                'class': "form-control",
                'style':'max-width: 300px',
                'placeholder': 'UserName'
                 }),
                'password':forms.PasswordInput(attrs={
                'class': "form-control",
                'style':'max-width: 300px',
                'placeholder': 'Password'
                 }),
                'fullname':forms.TextInput(attrs={
                'class': "form-control",
                'style':'max-width: 300px',
                'placeholder': 'Full Name'
                 }),
                'gender':forms.Select(attrs={
                'class': "form-control",
                'style':'max-width: 300px',
                'placeholder': 'Gender'
                 }),
                'dob':forms.DateTimeInput(attrs={
                'class': "form-control",
                'style':'max-width: 300px',
                'placeholder': 'dd/mm/yyyy'
                 }),
                'email':forms.EmailInput(attrs={
                'class': "form-control",
                'style':'max-width: 300px',
                'placeholder': 'Email'
                 }),
                'mobile':forms.NumberInput(attrs={
                'class': "form-control",
                'style':'max-width: 300px',
                'placeholder': 'MobileNumber'
                 }),
                'address':forms.Textarea(attrs={
                'class': "form-control",
                'style':'max-width: 300px',
                'placeholder': 'Address'
                 }),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=("__all__")
        widgets={
                'username':forms.TextInput(attrs={
                'class': "form-control",
                'style':'max-width: 300px',
                'placeholder': 'UserName'
                 }),
                  'username':forms.TextInput(attrs={
                'class': "form-control",
                'style':'max-width: 300px',
                'placeholder': 'UserName'
                 }),
                 

                }