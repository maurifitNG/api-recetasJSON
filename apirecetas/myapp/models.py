from django.db import models

# Create your models here.

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    preparation = models.TextField()
    people = models.IntegerField(default=1)
    onMenu = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name