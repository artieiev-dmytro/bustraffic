from django import forms

from .models import Bus
from cities.models import City


class BusForm(forms.ModelForm):
    name = forms.CharField(label='Bus', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the name of the bus',
    }))

    bus_time = forms.IntegerField(label='Time', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the time of the bus',
    }))

    from_city = forms.ModelChoiceField(label='From', 
        queryset=City.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control',})
    )

    to_city = forms.ModelChoiceField(label='To', 
        queryset=City.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control',})
    )

    class Meta:
        model = Bus
        fields = '__all__'