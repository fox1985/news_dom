# -*- coding: utf-8 -*-
from django import template
from listings.models import Category, Listing

register = template.Library()

@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all().filter(is_published=True)


@register.inclusion_tag('listings/tags/real_list.html')
def get_last_Listings(count=5):
    reals = Listing.objects.order_by("id").filter(is_published=True)[:count]
    return {"reals_list": reals}

