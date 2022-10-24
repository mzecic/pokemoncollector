from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    pokemon_type = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    height = models.IntegerField()

    def __str__(self):
        return self.name
