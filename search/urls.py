

from . import views
from django.urls import path



urlpatterns = [
    path('search/', views.search_form, name='search_results'),
]