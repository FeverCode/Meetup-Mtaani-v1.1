from re import A
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Deals)
admin.site.register(models.Profile)
admin.site.register(models.Reservation)
admin.site.register(models.NewsLetterRecepients)