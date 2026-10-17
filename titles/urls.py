from django.urls import path

from .views import(
  TitleListView,
  TitleCreateView,
  TitleUpdateView,
  TitleDeleteView,
)

urlpatterns = [
    path('', TitleListView.as_view(), name='title_list'),
    path('add/', TitleCreateView.as_view(), name='title_add'),
    path('<int:pk>/edit/', TitleUpdateView.as_view(), name='title_edit'),
    path('<int:pk>/delete/', TitleDeleteView.as_view(), name='title_delete'),
]
