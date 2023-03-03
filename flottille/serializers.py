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


class MedinaDockSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedinaDock
        fields = ['created_at']


class MyShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyShip
        fields = ['ship_name', 'medina_dock', 'spaceship', 'captain', 'xo']