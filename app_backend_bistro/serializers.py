from rest_framework import serializers
from .models import *


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'spice_level', 'category']


class OrderNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderName
        fields = ['id', 'name']




