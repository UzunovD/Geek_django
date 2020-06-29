from authapp.models import ShopUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.forms import HiddenInput


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
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control'
            field.help_text = ''


class ShopUserUpdateForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control'
            if field_name == 'password':
                field.widget = HiddenInput()
            field.help_text = ''


class ShopUserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = ShopUser
        fields =('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control'
            field.help_text = ''
