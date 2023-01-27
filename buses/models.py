from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

from cities.models import City


class Bus(models.Model):
    name = models.CharField(max_length=64, unique=True)
    bus_time = models.PositiveSmallIntegerField()
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city_set')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city_set')  

    def __str__(self):
        return self.name

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('city BAD')
        qs = self.__class__.objects.filter(from_city=self.from_city, to_city=self.to_city, 
            bus_time=self.bus_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('time BAD')

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('buses:detail', kwargs={'pk': self.id})

 