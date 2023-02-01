from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import City
from .forms import CityForm

__all__ = (
    'home', 
    'CityDetailView', 
    'CityCreateView', 
    'CityUpdateView',
    'CityDeleteView',
    'CityListView',
)

def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    form = CityForm()
    qs = City.objects.all()
    paginator = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    content = {
        'object_list': qs,
        'form': form,
        'page_obj': page_obj,
    }
    return render(request, 'cities/home.html', content)


class CityDetailView(DetailView):
    model = City
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = City
    template_name = 'cities/create.html'
    form_class = CityForm
    success_message = 'The city was successfully created'

class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = City
    template_name = 'cities/update.html'
    form_class = CityForm
    success_message = 'The city was successfully changed'


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'The city was successfully deleted')
        return self.post(request, *args, **kwargs)

class CityListView(ListView):
    paginate_by = 3
    model = City
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context

    def post(self, request):
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cities:home'))
