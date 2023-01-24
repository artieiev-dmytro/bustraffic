from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import City
from .forms import CityForm

__all__ = (
    'home', 
    'CityDetailView', 
    'CityCreateView', 
    'CityUpdateView',
    'CityDeleteView',
)

def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    form = CityForm()
    qs = City.objects.all()
    content = {
        'object_list': qs,
        'form': form,
    }
    return render(request, 'cities/home.html', content)


class CityDetailView(DetailView):
    model = City
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    template_name = 'cities/create.html'
    form_class = CityForm

class CityUpdateView(UpdateView):
    model = City
    template_name = 'cities/update.html'
    form_class = CityForm


class CityDeleteView(DeleteView):
    model = City
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)