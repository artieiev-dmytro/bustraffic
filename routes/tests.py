from django.test import TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse

from cities.models import City
from buses.models import Bus
from routes import views as route_view
from cities import views as cities_view

class AllTestsCase(TestCase):

    def setUp(self) -> None:
        self.city_A  = City.objects.create(name='A')
        self.city_B  = City.objects.create(name='B')
        self.city_C  = City.objects.create(name='C')
        self.city_D  = City.objects.create(name='D')
        self.city_E  = City.objects.create(name='E')

        lst = [
            Bus(name='b1', from_city=self.city_A, to_city=self.city_B, bus_time=9),
            Bus(name='b2', from_city=self.city_B, to_city=self.city_D, bus_time=8),
            Bus(name='b3', from_city=self.city_A, to_city=self.city_C, bus_time=7),
            Bus(name='b4', from_city=self.city_C, to_city=self.city_B, bus_time=6),
            Bus(name='b5', from_city=self.city_B, to_city=self.city_E, bus_time=3),
            Bus(name='b6', from_city=self.city_B, to_city=self.city_A, bus_time=11),
            Bus(name='b7', from_city=self.city_A, to_city=self.city_C, bus_time=10),
            Bus(name='b8', from_city=self.city_E, to_city=self.city_D, bus_time=5),
            Bus(name='b9', from_city=self.city_D, to_city=self.city_E, bus_time=4),
        ]

        Bus.objects.bulk_create(lst)

    def test_model_city_duplicate(self):

        city = City('A')
        with self.assertRaises(ValidationError):
            city.full_clean()

    def test_route_home_view(self):
        response = self.client.get(reverse('routes:home'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, template_name='routes/home.html')
        self.assertEqual(response.resolver_match.func, route_view.home)
    
    def test_cities_detail_view(self):
        response = self.client.get(reverse('cities:detail', kwargs={'pk': self.city_A.id}))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, template_name='cities/detail.html')
        self.assertEqual(response.resolver_match.func.__name__, cities_view.CityDetailView.as_view().__name__)