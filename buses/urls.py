from django.urls import path

from .views import *

urlpatterns = [
    #path('', home, name='home'),
    path('', BusListView.as_view(), name='home'),
    path('detail/<int:pk>/', BusDetailView.as_view(), name='detail'),
    path('add/', BusCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BusUpdateView.as_view(), name='update'),
    path('del/<int:pk>/', BusDeleteView.as_view(), name='delete'),
]