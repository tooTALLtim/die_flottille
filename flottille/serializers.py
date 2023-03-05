from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import *

class SpaceShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpaceShip
        fields = ['name', 'nickname', 'classification', 'armament', 'engine_type', 'description']


class CrewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Crew
        fields = ['first_name', 'last_name', 'nickname', 'origin', 'description', 'staff_level']


class MyShipSerializer(WritableNestedModelSerializer): #like CartItem
    spaceship = SpaceShipSerializer()
    captain = CrewSerializer()
    xo = CrewSerializer()

    class Meta:
        model = MyShip
        fields = ['id', 'ship_name', 'medina_dock', 'spaceship', 'captain', 'xo']
     
    #DRF way
    # def save(self, validated_data):
    #     spaceship_data = validated_data.pop('spaceship')
    #     my_ship = MyShip.objects.create(**spaceship_data)
    #     SpaceShip.objects.create(my_ship=my_ship, **validated_data)
    #     return my_ship

    # 
    # def create(self, validated_data):
    #     spaceship_data = SpaceShip.objects.get(pk=validated_data.pop('spaceship'))
    #     SpaceShip.objects.create(my_spaceship=my_spaceship, **spaceship_data)
    #     my_spaceship = MyShip.objects.create(**validated_data)
    #     return my_spaceship

    # SO second way
    # def create(self, validated_data):
    #     spaceship_data = validated_data.pop('spaceship')
    #     spaceship_model = SpaceShip.objects.create(**spaceship_data)
    #     my_ship = MyShip.objects.create(spaceship=spaceship, **validated_data)
    #     return my_ship



# class AddMyShipSerializer(serializers.ModelSerializer):

#     def save(self, **kwargs):
#         medina_dock_id = self.context['medina_dock_id']
        

#         # try:
#         #     my_ship = MyShip.objects.get(
#         #         medina_dock_id = medina_dock_id,
#         #     )
#         #     my_ship.save()
#         #     self.instance = my_ship
#         # except MyShip.DoesNotExist:
            

#     class Meta:
#         model = MyShip
#         fields = ['id', 'ship_name', 'spaceship', 'captain', 'xo']


class MedinaDockSerializer(serializers.ModelSerializer): #like Cart
    id = serializers.UUIDField(read_only=True)
    my_ships = MyShipSerializer(many=True, read_only=True)

    class Meta:
        model = MedinaDock
        fields = ['id', 'created_at', 'my_ships']

