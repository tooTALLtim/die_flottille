from django.urls import path
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register('spaceships', SpaceShipViewSet)
router.register('crews', CrewViewSet)
router.register('medina_docks', MedinaDockViewSet)

medina_dock = routers.NestedDefaultRouter(
    router, 'medina_docks', lookup='medina_dock')
medina_dock.register(
    'my_ships', MyShipViewSet, basename='medina_dock-my_ships')


urlpatterns = router.urls + medina_dock.urls