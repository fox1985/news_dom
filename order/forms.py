from django import forms
from .models import Order
from listings.models import Listing
from django.forms import Textarea
from captcha.fields import CaptchaField
from realtors.models import Realtor

class OrderForm(forms.ModelForm):
    listing = forms.ModelChoiceField(queryset=Listing.objects.all(), widget=forms.HiddenInput())
    captcha = CaptchaField(label='Введите текст с картинки',error_messages={'invalid': 'Неправильный текст'})
    class Meta:
        model = Order
        fields = ['listing', 'name', 'email', 'nomer', 'telephone', 'text']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'nomer': forms.TextInput(attrs={"class": "form-control"}),
            'telephone': forms.TextInput(attrs={"class": "form-control"}),
            'text': Textarea(attrs={'cols': 25, 'rows': 5, "class": "form-control", "style": 'margin-top: 0px; margin-bottom: 0px; height: 200px;'}),
        }

