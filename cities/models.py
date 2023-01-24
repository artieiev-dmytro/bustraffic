from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=64, unique=True)


    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk': self.id})