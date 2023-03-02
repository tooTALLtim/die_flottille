from django.db import models


class SpaceShip(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Captain(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=100, default='no nicknames found')
    origin = models.CharField(max_length=50, default='unknown origin')
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class XO(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=100, default='no nicknames found')
    origin = models.CharField(max_length=50, default='unknown origin')
    description = models.TextField()

    def __str__(self):
        return f'{first_name} {self.last_name}'


