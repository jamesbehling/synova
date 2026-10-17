from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('employees/',include('employees.urls')),
    path('employeeassignments/',include('employeeassignments.urls')),
    path('houses/',include('houses.urls')),
    path('reports/',include('reports.urls')),
    path('titles/',include('titles.urls')),
]
