from django import forms
from django.core import validators


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator()
        ]
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'The Password And Password Repetition Are Inconsistent.')
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator()
        ]
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
