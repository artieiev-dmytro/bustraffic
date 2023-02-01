from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('routes.urls', 'routes'))),
    path('cities/', include(('cities.urls', 'cities'))),
    path('buses/', include(('buses.urls', 'buses'))),
    path('accounts/', include(('accounts.urls', 'accounts'))),
]
