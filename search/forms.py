# -*- coding: utf-8 -*-
from django import forms


class HousesFilterForm(forms.Form):
    """поиск на сайте
    required=False поля не обезательно для запланения
    """
    category = forms.CharField(label='Категория', max_length=200, required=False, )
    min_price = forms.CharField(label="цена от", required=False, max_length=200)
    max_price = forms.CharField(label="цена до", required=False, max_length=200,)
    rooms = forms.IntegerField(label='Комнат', required=False, )
    bathrooms = forms.IntegerField(label='Санузел', required=False,)
    bedrooms = forms.IntegerField(label='спальни', required=False, )
    sqft = forms.IntegerField(label='Квадратные метры', required=False)
    city = forms.CharField(label='Город', required=False,)
