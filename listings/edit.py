# -*- coding: utf-8 -*-
from django.urls import reverse_lazy
from .models import Listing, Galary_image
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView, ProcessFormView
from  listings.forms import Form_Listing



class Form_Galary_View(FormView):
    """Добавления товара через форму"""
    form_class = Form_Listing
    template_name = 'edit/new_page.html'
    success_url = '/'  # переадресация на страницу в случае успешной отправки

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        galary_image = request.FILES.getlist('galary_image')
        if form.is_valid():
            pk = form.save().pk
            Listing_page = Listing.objects.get(pk=pk)
            if galary_image:
                for f in galary_image:
                    fl = Galary_image(Listing_page=Listing_page, galary_image=f)
                    fl.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)




class Realty_PageUpdate(UpdateView,):
    """редактировать товар"""
    model = Listing
    template_name = "edit/edit_page.html"
    pk_url_kwarg = "listing_id"

    success_url = '/'

    fields = ['realtor', 'title', 'address', 'district', 'region', 'rooms', 'sale_and_rental',  'from_the_sea', 'city', 'state',  'description', 'price', 'bedrooms',
                  'bathrooms', 'garage', 'floors', 'sqft', 'land_area', 'terrace_area', 'lot_size', 'vid_name', 'tip_name', 'page_info', 'photo_main',  'is_published',]






