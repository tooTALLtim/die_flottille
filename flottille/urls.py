from django.urls import path
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register('spaceships', SpaceShipViewSet)
router.register('crews', CrewViewSet)

urlpatterns = router.urls