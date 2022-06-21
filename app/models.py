from unicodedata import name
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class MtaaniDeals(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    location = models.CharField(max_length=255)
    
    def __str__(self):
            return self.name

class Reservation(models.Model):
    numberOfPeople = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, unique=True)
    time = models.TimeField(null=False, blank=False, unique=True)
    
    
    
    
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    email= models.EmailField(max_length=255, unique=True)
    photo = CloudinaryField('image', default='https://res.cloudinary.com/fevercode/image/upload/v1654534329/default_n0r7rf.png')
    name = models.CharField(max_length=255)
    Tel = models.IntegerField(null=False, unique=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

class NewsLetterRecepients(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()


    
    