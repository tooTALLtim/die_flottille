from django.db import models
from uuid import uuid4


class SpaceShip(models.Model):
    """
    The bones of greatness are what you make it,
    choose your vessel wisely.
    """
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)
    classification = models.CharField(max_length=50)
    armament = models.TextField(max_length=300)
    engine_type = models.TextField(max_length=60)
    description = models.TextField()


    def __str__(self):
        return self.name


class Crew(models.Model):
    """
    Those who choose to go into the darkness and 
    inhospitable vacuum of space...don't like Earth.
    """

    class StaffLevel(models.TextChoices):
        UNASSIGNED = 'unassigned', 'UNASSIGNED'
        ADMIRAL = 'admiral', 'ADMIRAL'
        CAPTAIN = 'captain', 'CAPTAIN'
        EXECUTIVE_OFFICER = 'XO', 'XO'
        #put more choices here after testing


    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=100, default='no nicknames known')
    origin = models.CharField(max_length=50, default='unknown origin')
    description = models.TextField(max_length=400)
    staff_level = models.CharField(
                    max_length=20, 
                    choices=StaffLevel.choices, 
                    default=StaffLevel.UNASSIGNED)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class MedinaDock(models.Model): #like Cart
    """
    A place to dock your ship, assemble your crew, and more.
    """
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class MyShip(models.Model): #like CartItem
    """
    The components of your Medina dock.
    """
    ship_name = models.CharField(max_length=60)
    medina_dock = models.ForeignKey(
        MedinaDock, on_delete=models.CASCADE, related_name='my_dock')
    spaceship = models.ForeignKey(
        SpaceShip, on_delete=models.CASCADE, related_name='my_spaceship')
    captain = models.ForeignKey(
        Crew, on_delete=models.CASCADE, related_name='my_captain')
    xo = models.ForeignKey(
        Crew, on_delete=models.CASCADE, related_name='my_xo')
    
    def __str__(self):
        return self.ship_name