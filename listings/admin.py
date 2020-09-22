

# Register your models here.

from django.contrib import admin

# Register your models here.
from .models import Listing, Info, Galary_image, Category

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_published', )
  list_editable = ('is_published',)

class Galary_image_Admin(admin.TabularInline):
  model = Galary_image
  extra = 4



class ListingAdmin(admin.ModelAdmin):
  inlines = [Galary_image_Admin]
  list_display = ('id', 'title', 'is_published', 'floors', 'price', 'list_date', 'realtor', 'land_area', 'terrace_area', 'contact')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state',  'price')
  list_per_page = 25





admin.site.register(Listing, ListingAdmin)
admin.site.register(Info)
admin.site.register(Category, CategoryAdmin)