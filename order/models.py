from django.db import models

# Create your models here.
from datetime import datetime
from  listings.models import Listing
from realtors.models import Realtor



from django.db import models


# Create your models here.
class Order(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField()
    nomer = models.CharField(max_length=100, verbose_name='Номер ID')
    telephone = models.CharField(max_length=100, verbose_name='Телефон')
    text = models.TextField(verbose_name='Сообщения',)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)








    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
