from django import forms
from .models import Account
from django.contrib.auth import password_validation


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)

    last_name = forms.CharField(max_length=100)

    phone_number = forms.CharField(max_length=50)

    email = forms.EmailField(max_length=50)

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
                               help_text=password_validation.password_validators_help_text_html)

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Mật khẩu không hợp lệ!'
            )
        password_validation.validate_password(self.cleaned_data.get('password'), None)
