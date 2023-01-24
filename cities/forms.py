from django import forms

from .models import City

class CityForm(forms.ModelForm):
    name = forms.CharField(label='City', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the name of the city',
    }))

    class Meta:
        model = City
        fields = ('name',)

