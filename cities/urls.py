from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add/', CityCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('del/<int:pk>/', CityDeleteView.as_view(), name='delete'),
]
