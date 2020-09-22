
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse

from listings.models import Listing, Category, Galary_image
from django.contrib import auth
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect




# Create your views here.
from order.forms import OrderForm
from order.models import Order


def listings(request,):
    """Главная страныица listings"""
    listings = Listing.objects.order_by('price').filter(is_published=True,)
    paginator = Paginator(listings, 100)  # выводит сколько страници  должно быть до погинации
    # подключиение пагинацыи
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
      page_obj = paginator.page(paginator.num_pages)

    context = {'listings': page_obj,}
    return render(request, 'listings/listings.html', context)


def category_page(request, cat_id):
  """Выборка категорий
    1 создать словарь
    2 выбрать отну страницу из категории#филтрует категорию выбирает категорию
    3 выводить из базы через словарь имя категории
    4 фильтровать страницу и категории
    5 выводить страницы через словарь
  """
  context_dict = {}


  category = Category.objects.get(pk=cat_id)  # выбрать одну категорию

  context_dict['category_name'] = category.name  # Вытошеть имя категории

  listings = Listing.objects.filter(category=category).prefetch_related('galary_image_set').all()

  paginator = Paginator(listings, 6)  # выводит сколько страници  должно быть до погинации

  # подключиение пагинацыи
  page = request.GET.get('page')
  try:
    page_obj = paginator.page(page)
  except PageNotAnInteger:

    page_obj = paginator.page(1)
  except EmptyPage:

    page_obj = paginator.page(paginator.num_pages)
  # подключиение пагинацыи

  context_dict['listings'] = page_obj  # для вывода страницы

  context_dict['galary_image'] = Galary_image.objects.filter(pk=cat_id)  # Филтует галирею изображений

  context_dict['username'] = auth.get_user(request).username  # Афторизация пользователя



  return render(request, 'listings/category.html', context_dict)







def listing(request, listing_id):
  """Страница listing"""
  listing = get_object_or_404(Listing, pk=listing_id)
  form = OrderForm(request.POST or None, initial={'listing': listing} )

  if request.method == "POST":
    if form.is_valid():
      form.save()

      send_mail('Заявка от torrehome.ru', 'Зайдите в админку чтобы почетать заявку',  'torrehome.ru/admin/',
                ['artemdav2@gmail.com'], fail_silently=False)
      return  HttpResponseRedirect("{}?sended=True".format(reverse('listing', kwargs={'listing_id': listing_id})), )




  context = {
    'listing': listing,
    'form' : form,
    'sended': request.GET.get("sended", False)
  }

  return render(request, 'listings/listing.html', context)
