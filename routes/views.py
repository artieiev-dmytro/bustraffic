from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView

from .forms import RouteForm, RouteModelForm
from .utils import get_routes
from .models import Route
from buses.models import Bus
from cities.models import City

__all__ = (
    'home',
    'find_routes',
    'add_route',
    'save_route',
    'RouteListView'
)

def home(request):
    form = RouteForm()
    context = {
        'form': form,
    }
    return render(request, 'routes/home.html', context)


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'No data to search')
        context = {
            'form': form,
        }
        return render(request, 'routes/home.html', context) 


def add_route(request):
    if request.method == 'POST':
        context = {}
        data =request.POST
        if data:

            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            total_time = int(data['total_time'])
            buses = [int(i) for i in data['buses'].split(',') if i.isdigit()]
            qs = Bus.objects.filter(id__in=buses).select_related('from_city', 'to_city')
            cities = City.objects.filter(id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(
                initial={
                    'from_city': cities[from_city_id],
                    'to_city': cities[to_city_id],
                    'route_time': total_time,
                    'buses': qs,
                }
            )
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, 'No data  -- -- to search')
        return redirect('routes:home')


def save_route(request):
    if request.method == 'POST':
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Goot')
            return redirect('routes:home')
        
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, 'No data  -- -- to search')
        return redirect('routes:home')


class RouteListView(ListView):
    paginate_by = 3
    model = Route
    template_name = 'routes/list.html'