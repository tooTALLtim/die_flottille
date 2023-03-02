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


    def __str__(self):
        return self.name


class Captain(models.Model):
    """
    Someone's gotta make the decisions and get the blame,
    let's find you a captain!
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=100, default='no nicknames found')
    origin = models.CharField(max_length=50, default='unknown origin')
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class XO(models.Model):
    """
    A captain is only as good as the crew that serves with them,
    and that starts with a good Executive Officer.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=100, default='no nicknames found')
    origin = models.CharField(max_length=50, default='unknown origin')
    description = models.TextField()

    def __str__(self):
        return f'{first_name} {self.last_name}'


class MedinaDock(models.Model):
    """
    A place to dock your ship, assemble your crew, and more.
    """
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class MyShip(models.Model):
    """
    The components of your Medina dock.
    """
    ship_name = models.CharField(max_length=60)
    medina_dock = models.ForeignKey(
        MedinaDock, on_delete=models.CASCADE, related_name='medina_dock')
    spaceship = models.ForeignKey(
        SpaceShip, on_delete=models.CASCADE, related_name='spaceship')
    captain = models.ForeignKey(
        Captain, on_delete=models.CASCADE, related_name='captain')