from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView

from .models import City

__all__ = (
    'home', 'CityDetailView',
)

def home(request, pk=None):
    if pk:
        city = get_object_or_404(City, id=pk)
        content = {'object': city}
        return render(request, 'cities/detile.html', content)
    qs = City.objects.all()
    content = {
        'object_list': qs,
    }
    return render(request, 'cities/home.html', content)


class CityDetailView(DetailView):
    model = City
    template_name = 'cities/detail.html'