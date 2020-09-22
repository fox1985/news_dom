
from django.db import models
from datetime import datetime
from django.contrib import messages, auth
from django.contrib.auth.models import User

class Realtor(models.Model):
  name = models.CharField(max_length=200, blank=True)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20,)
  email = models.CharField(max_length=50)
  is_mvp = models.BooleanField(default=False)
  hire_date = models.DateTimeField(default=datetime.now, blank=True)

  class Meta:
    verbose_name = 'риэлтор'
    verbose_name_plural = 'риэлторы'


  def __str__(self):
    return self.name
