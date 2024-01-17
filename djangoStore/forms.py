from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from djangoStore.models import Product
from .models import Refund
from django.contrib.auth.forms import UserCreationForm

class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user is None:
                raise forms.ValidationError(_("Invalid username or password"))

            cleaned_data['authenticated_user'] = user

        return cleaned_data


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class FormCreate(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_discription', 'product_price', 'product_amount', 'product_image']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"



class ReturnRequestForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = []


class ReturnRequestAdminForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = ['approved', 'rejected']

    return_request_id = forms.IntegerField(widget=forms.HiddenInput())

