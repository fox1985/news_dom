

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import  edit

urlpatterns = [

    path('', views.listings, name='listings'),

    path('category/<int:cat_id>/', views.category_page, name='category_page'),#Выборка категорий

    path('listing/<int:listing_id>', views.listing, name='listing'),

    path('add', edit.Form_Galary_View.as_view(), name="new_page"),# Добавить товар

    path('listing/<listing_id>/edit/', edit.Realty_PageUpdate.as_view(), name='edit_page'),# редактировать товар



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)