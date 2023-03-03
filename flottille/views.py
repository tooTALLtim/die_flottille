from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


def hello(request):
    return render(request, 'hello.html')


class SpaceShipViewSet(ModelViewSet):
    queryset = SpaceShip.objects.all()
    serializer_class = SpaceShipSerializer