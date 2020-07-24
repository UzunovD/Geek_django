import random, hashlib

import django.forms as forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, \
    UserChangeForm, PasswordChangeForm
from django.forms import HiddenInput

from authapp.models import ShopUser, ShopUserProfile


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("You are too young!")
        return data

    def save(self, commit=True):
        user = super(ShopUserRegisterForm, self).save()

        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[
               :10]
        user.activation_key = hashlib.sha1((user.email + salt).encode(
            'utf-8')).hexdigest()
        user.save()

        return user


class ShopUserUpdateForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = (
        'username', 'password', 'email', 'first_name', 'last_name', 'age',
        'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control'
            if field_name == 'password':
                field.widget = HiddenInput()
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("You are too young!")
        return data


class ShopUserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ShopUserProfile
        fields = ('tagline', 'aboutMe', 'gender',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class ShopUserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = ShopUser
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control'
            field.help_text = ''
