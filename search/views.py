# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render
from search.forms import HousesFilterForm
from listings.models import Listing, Category

"""
gt
Больше чем.
---------------
gte
Больше чем или равно.
-------------------------
lt
Меньше чем.
-----------------------------

lte
Меньше чем или равно.
------------------------------------

exact
Точное совпадение.

"""



def search_form(request):
    """Поиск на сайте"""
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    categorys = Category.objects.order_by('name').filter(is_published=True)


    'поиск на сайте'
    housesform = HousesFilterForm(request.GET)
    if housesform.is_valid():
        if housesform.cleaned_data['max_price']:
            'Поиск по ценам'
            listings = listings.filter(Q(price__lte=housesform.cleaned_data['min_price']) | Q(price__lte=housesform.cleaned_data['max_price']))

        if housesform.cleaned_data['min_price']:
            'Поиск по ценам'
            listings = listings.filter(Q(price__gte=housesform.cleaned_data['min_price']) | Q(price__gte=housesform.cleaned_data['max_price']))





#-----------------------------------------------------------------------------------------------------------------------

        if housesform.cleaned_data['sqft']:
            'Квадратные метры Больше или равно'
            listings = listings.filter(sqft__gte=housesform.cleaned_data['sqft'])

        if housesform.cleaned_data['sqft']:
            'Квадратные метры или аренда меньше или равно'
            listings = listings.filter(sqft__lte=housesform.cleaned_data['sqft'])
#-----------------------------------------------------------------------------------------------------------------------

        if housesform.cleaned_data['bedrooms']:
            'спальни больше или равно'
            listings = listings.filter(bedrooms__gte=housesform.cleaned_data['bedrooms'])



        if housesform.cleaned_data['bedrooms']:
            'спальни менше или равно'
            listings = listings.filter(bedrooms__lte=housesform.cleaned_data['bedrooms'])
#---------------------------------------------------------------------------------------------------------------------

        if housesform.cleaned_data['city']:
            'Город'
            listings = listings.filter(city__icontains=housesform.cleaned_data['city'])

#---------------------------------------------------------------------------------------------------------------------

        if housesform.cleaned_data['category']:
            'Вид недвижимости'
            listings = listings.filter(category__name=housesform.cleaned_data['category'])



    context = {'listings': listings, 'category': categorys, 'housesform': housesform}
    return render(request, 'listings/listings.html', context)

