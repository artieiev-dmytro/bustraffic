from django import forms

from cities.models import City
from .models import Route


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='From', 
        queryset=City.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control single',})
    )

    to_city = forms.ModelChoiceField(label='To', 
        queryset=City.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control single',})
    )

    cities = forms.ModelMultipleChoiceField(
        label='Through', 
        queryset=City.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control multiple',})
    )

    time = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'время в пути'})
    )


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label='Route', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the name of the route',
        }))

    from_city = forms.ModelChoiceField(
        queryset=City.objects.all(), 
        widget=forms.HiddenInput()
    )

    to_city = forms.ModelChoiceField( 
        queryset=City.objects.all(), 
        widget=forms.HiddenInput()
    )

    buses = forms.ModelMultipleChoiceField( 
        queryset=City.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control d-none',})
    )

    route_time = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Route
        fields = '__all__'

