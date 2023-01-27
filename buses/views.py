from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


from .models import Bus
from .forms import BusForm

__all__ = (
    'home', 
    'BusDetailView', 
    'BusCreateView', 
    'BusUpdateView',
    'BusDeleteView',
    'BusListView',
)

def home(request, pk=None):
    qs = Bus.objects.all()
    paginator = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    content = {
        'object_list': qs,
        'page_obj': page_obj,
    }
    return render(request, 'cities/home.html', content)


class BusDetailView(DetailView):
    model = Bus
    template_name = 'buses/detail.html'


class BusCreateView(SuccessMessageMixin, CreateView):
    model = Bus
    template_name = 'buses/create.html'
    form_class = BusForm
    success_message = 'The bus was successfully created'


class BusUpdateView(SuccessMessageMixin, UpdateView):
    model = Bus
    template_name = 'buses/update.html'
    form_class = BusForm
    success_message = 'The city was successfully changed'


class BusDeleteView(DeleteView):
    model = Bus
    success_url = reverse_lazy('buses:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'The bus was successfully deleted')
        return self.post(request, *args, **kwargs)


class BusListView(ListView):
    paginate_by = 3
    model = Bus
    template_name = 'buses/home.html'



