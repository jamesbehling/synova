from django.urls import path

from .views import(
  EmployeeAssignmentListView,
  EmployeeAssignmentCreateView,
  EmployeeAssignmentUpdateView,
  EmployeeAssignmentDeleteView,
)

urlpatterns = [
    path('', EmployeeAssignmentListView.as_view(), name='employeeassignment_list'),
    path('add/', EmployeeAssignmentCreateView.as_view(), name='employeeassignment_add'),
    path('<int:pk>/edit/', EmployeeAssignmentUpdateView.as_view(), name='employeeassignment_edit'),
    path('<int:pk>/delete/', EmployeeAssignmentDeleteView.as_view(), name='employeeassignment_delete'),
]
