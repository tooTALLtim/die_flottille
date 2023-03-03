from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class SpaceShipViewSet(ModelViewSet):
    queryset = SpaceShip.objects.all()
    serializer_class = SpaceShipSerializer


class CrewViewSet(ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class MedinaDockViewSet(ModelViewSet):
    queryset = MedinaDock.objects.all()
    serializer_class = MedinaDockSerializer


class MyShipViewSet(ModelViewSet):
    queryset = MyShip.objects.all()
    serializer_class = MyShipSerializer