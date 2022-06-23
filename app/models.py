from __future__ import unicode_literals
from queue import Empty
from random import choices
from unicodedata import name
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.forms import ChoiceField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Deals(models.Model):
    CHOICE = (
    ('She is mine deals', 'She is mine deals'),
    ('Picnic in a Nick', 'Picnic in a Nick'),
    ('Workspace deals', 'Workspace deals'),
    )
    name = models.CharField(max_length=200, choices=CHOICE, blank=True)
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
        
    def update_Deals(self, new_choice):
        self.deal = new_choice
        self.save()
        
    @classmethod
    def search_by_name(cls, search_term):
        deal = cls.objects.filter(name=search_term)
        return deal

class Reservation(models.Model):
    deal = models.ForeignKey(Deals, on_delete=models.CASCADE,related_name='deal')
    numberOfPeople = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, unique=True)
    time = models.TimeField(null=False, blank=False, unique=True)
    
    
    def __str__(self):
        return str(self.deal)
    
    def create_reservation(self):
        self.save()
    
    def delete_reservation(self):
        self.delete()
        
    def update_reservation(self, new_deal):
        self.name = new_deal
        self.save()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email= models.EmailField(max_length=255)
    photo = CloudinaryField('image', default='https://res.cloudinary.com/fevercode/image/upload/v1654534329/default_n0r7rf.png')
    name = models.CharField(max_length=255, blank=True)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    location = models.CharField(max_length=255 )
    bio = models.TextField(max_length=500, default='This is my bio')
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def create_profile(self):
        self.save()
        
    def update_profile(self, new_bio):
        self.bio = new_bio
        self.save()

class NewsLetterRecepients(models.Model):
    name = models.CharField(max_length=255, null=False,blank=False)
    email = models.EmailField()


class AccessToken(models.Model):
	token = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		get_latest_by = 'created_at'

	def __str__(self):
		return self.token
