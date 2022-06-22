from types import new_class
from unicodedata import name
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
DEALS_CHOICES = [
    ('She is mine deals', 'She is mine deals'),
    ('Picnic in a Nick', 'Picnic in a Nick'),
    ('Worksapce deals', 'Worksapce deals'),
]
class Deals(models.Model):
    deal = models.CharField(max_length=255, choices=DEALS_CHOICES, blank=True)
    description = models.TextField()
    photo = CloudinaryField('Image')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    location = models.CharField(max_length=255)
    
    def __str__(self):
            return self.name
        
    def create_Deals(self):
        self.save()
        
    def delete_Deals(self):
        self.delete()
        
    def update_Deals(self, new_reservation):
        self.name = new_reservation
        self.save()
        
    @classmethod
    def search_by_name(cls, search_term):
        deal = cls.objects.filter(name=search_term)
        return deal

class Reservation(models.Model):
    deal = models.ForeignKey(Deals, on_delete=models.SET_NULL, choices=DEALS_CHOICES, null=True)
    numberOfPeople = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, unique=True)
    time = models.TimeField(null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.reservation
    
    def create_reservation(self):
        self.save()
    
    def delete_reservation(self):
        self.delete()
        
    def update_reservation(self, new_reservation):
        self.name = new_reservation
        self.save()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email= models.EmailField(max_length=255)
    photo = CloudinaryField('image', default='https://res.cloudinary.com/fevercode/image/upload/v1654534329/default_n0r7rf.png')
    name = models.CharField(max_length=255)
    Tel = models.IntegerField(null=True, unique=True)
    location = models.CharField(max_length=255 )
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(max_length=500, default='This is my bio')
    def __str__(self):
        return f'{self.user.username} Profile'

class NewsLetterRecepients(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()


    
    