from django.db import models


class Ship(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)


class Captain(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=100, default='no nicknames found')
    origin = models.CharField(max_length=50, default='unknown origin')
    description = models.TextField()


class XO(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=100, default='no nicknames found')
    origin = models.CharField(max_length=50, default='unknown origin')
    description = models.TextField()


