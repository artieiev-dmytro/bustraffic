from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('find_routes/', find_routes, name='find_routes'), 
    path('add_routes/', add_route, name='add_route'),
    path('save_routes/', save_route, name='save_route'),
    path('list/', RouteListView.as_view(), name='list')
]