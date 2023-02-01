from django.db import models

from cities.models import City
from buses.models import Bus


class Route(models.Model):
    name = models.CharField(max_length=64, unique=True)
    route_time = models.PositiveSmallIntegerField()
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_to_city_set')
    buses = models.ManyToManyField(Bus)  

    def __str__(self):
        return self.name 