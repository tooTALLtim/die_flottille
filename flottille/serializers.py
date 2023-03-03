from rest_framework import serializers
from .models import *

class SpaceShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpaceShip
        fields = ['name', 'nickname', 'classification', 'armament', 'engine_type']


class CrewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Crew
        fields = ['first_name', 'last_name', 'nickname', 'origin', 'description', 'staff_level']