from . models import Deals
from rest_framework import serializers
from django.contrib.auth.models import User


class DealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals
        fields = ('name', 'description', 'photo', 'price', 'location')
