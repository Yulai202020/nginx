from django.db import models

class Persons(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
