
from django.contrib import admin
from order.models import Order

# Register your models here.
@admin.register(Order)
class AdmeinOrder(admin.ModelAdmin):
    list_display = ('listing', 'name', 'email', 'nomer', 'telephone', 'text' )
    ordering = ['listing',]