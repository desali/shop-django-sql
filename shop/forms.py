from django import forms
from django.contrib.auth.models import User

from .models import Admin, Category, Product, Customer


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ('login', 'password')


class CustomerLoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('email', 'password')


class CategoryNewForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description')


class ProductNewForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'count', 'price')
