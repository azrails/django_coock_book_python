from django.db import models
from django.utils import timezone
from django.conf import settings

class Recipe(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=105)
    formula = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ingridients = models.ManyToManyField('Ingridient', related_name='recipes')
    
    def __str__(self) -> str:
        return self.title


class Ingridient(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.title