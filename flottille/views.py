from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class SpaceShipViewSet(ModelViewSet):
    queryset = SpaceShip.objects.all()
    serializer_class = SpaceShipSerializer