from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authapp.forms import forms
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class AddCSSClassFormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ChekAge18Mixin:
    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("User is too young!")
        return data


class AdminShopUserCreateForm(AddCSSClassFormControlMixin, ChekAge18Mixin, UserCreationForm):
    class Meta:
        model = ShopUser
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser', 'is_staff',
            'password1', 'password2', 'email', 'age', 'avatar'
        )


class AdminShopUserUpdateForm(AddCSSClassFormControlMixin, ChekAge18Mixin, UserChangeForm):
    class Meta:
        model = ShopUser
        # fields = '__all__'
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'password', 'email', 'age', 'avatar', 'is_active', 'is_staff'
        )


class AdminProductCategoryEditForm(AddCSSClassFormControlMixin, forms.ModelForm):
    discount = forms.IntegerField(label='discount', required=False,
                                  min_value=-90, max_value=90, initial=0)
    class Meta:
        model = ProductCategory
        fields = '__all__'


class AdminProductEditForm(AddCSSClassFormControlMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
