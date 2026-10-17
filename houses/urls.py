from django.urls import path

from .views import(
  HouseListView,
  HouseCreateView,
  HouseUpdateView,
  HouseDeleteView,
)

urlpatterns = [
    path('', HouseListView.as_view(), name='house_list'),
    path('add/', HouseCreateView.as_view(), name='house_add'),
    path('<int:pk>/edit/', HouseUpdateView.as_view(), name='house_edit'),
    path('<int:pk>/delete/', HouseDeleteView.as_view(), name='house_delete'),
]
