from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('reports/',include('reports.urls')),
    path('employees/',include('employees.urls')),
]
