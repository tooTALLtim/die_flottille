from rest_framework import serializers
from .models import *

class SpaceShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpaceShip
        fields = ['name', 'nickname', 'classification', 'armament', 'engine_type', 'description']


class CrewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Crew
        fields = ['first_name', 'last_name', 'nickname', 'origin', 'description', 'staff_level']


class MyShipSerializer(serializers.ModelSerializer): #like CartItem

    class Meta:
        model = MyShip
        fields = ['id', 'ship_name', 'medina_dock', 'spaceship', 'captain', 'xo']


class AddMyShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyShip
        fields = ['id', 'ship_name', 'spaceship', 'captain', 'xo']


class MedinaDockSerializer(serializers.ModelSerializer): #like Cart
    id = serializers.UUIDField(read_only=True)
    my_ship = MyShipSerializer(many=True, read_only=True)

    class Meta:
        model = MedinaDock
        fields = ['id', 'created_at', 'my_ship']

