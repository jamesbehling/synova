from django.urls import path
from .views import (
    CarListView, CarCreateView, CarUpdateView, CarDeleteView, CarDetailView,
    MaintenanceCreateView
)

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('add/', CarCreateView.as_view(), name='car_add'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('<int:pk>/edit/', CarUpdateView.as_view(), name='car_edit'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    path('<int:car_pk>/maintenance/add/', MaintenanceCreateView.as_view(), name='maintenance_add'),
]
