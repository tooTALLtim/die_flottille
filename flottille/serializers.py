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
    spaceship = SpaceShipSerializer()
    captain = CrewSerializer()
    xo = CrewSerializer()

    class Meta:
        model = MyShip
        fields = ['id', 'ship_name', 'medina_dock', 'spaceship', 'captain', 'xo']


class AddMyShipSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        medina_dock_id = self.context['medina_dock_id']
        

        # try:
        #     my_ship = MyShip.objects.get(
        #         medina_dock_id = medina_dock_id,
        #     )
        #     my_ship.save()
        #     self.instance = my_ship
        # except MyShip.DoesNotExist:
            

    class Meta:
        model = MyShip
        fields = ['id', 'ship_name', 'spaceship', 'captain', 'xo']


class MedinaDockSerializer(serializers.ModelSerializer): #like Cart
    id = serializers.UUIDField(read_only=True)
    my_ships = MyShipSerializer(many=True, read_only=True)

    class Meta:
        model = MedinaDock
        fields = ['id', 'created_at', 'my_ships']

