from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class SpaceShipViewSet(ModelViewSet):
    queryset = SpaceShip.objects.all()
    serializer_class = SpaceShipSerializer


class CrewViewSet(ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class MedinaDockViewSet(ModelViewSet): #like Cart
    queryset = MedinaDock.objects.all()
    serializer_class = MedinaDockSerializer


class MyShipViewSet(ModelViewSet): #like CartItem
    serializer_class = MyShipSerializer

    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return AddMyShipSerializer
    #     else:
    #         return MyShipSerializer
    
    def get_serializer_context(self):
        return {'medina_dock_id': self.kwargs['medina_dock_pk']}

    def get_queryset(self):
        return MyShip.objects \
                .filter(medina_dock_id=self.kwargs['medina_dock_pk'])
