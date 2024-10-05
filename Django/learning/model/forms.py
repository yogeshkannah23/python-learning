from model.models import *
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'