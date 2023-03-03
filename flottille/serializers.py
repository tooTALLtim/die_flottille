from rest_framework import serializers
from .models import *

class SpaceShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpaceShip
        fields = ['name', 'nickname', 'classification', 'armament', 'engine_type']