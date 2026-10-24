from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect

from django.views.generic import (
  ListView,
  CreateView,
  UpdateView,
  DeleteView,
)

from django.urls import reverse_lazy
from .models import EmployeeAssignment

class EmployeeAssignmentListView(ListView):
    model = EmployeeAssignment
    template_name = 'employeeassignments/employeeassignment_list.html'

class EmployeeAssignmentCreateView(CreateView):
    model = EmployeeAssignment
    fields = '__all__'
    template_name = 'employeeassignments/employeeassignment_form.html'
    success_url = reverse_lazy('employeeassignment_list')

class EmployeeAssignmentUpdateView(UpdateView):
    model = EmployeeAssignment
    fields = '__all__'
    template_name = 'employeeassignments/employeeassignment_form.html'
    success_url = reverse_lazy('employeeassignment_list')

class EmployeeAssignmentDeleteView(DeleteView):
    model = EmployeeAssignment
    template_name = 'employeeassignments/employeeassignment_delete.html'
    success_url = reverse_lazy('employeeassignment_list')

class EmployeeAssignmentDeleteView(DeleteView):
    model = EmployeeAssignment
    template_name = 'employeeassignments/employeeassignment_delete.html'
    success_url = reverse_lazy('employeeassignment_list') # Or use reverse_lazy('employeeassignment_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                "Cannot delete this employeeassignment because one or more employees (like James Behling) are still assigned to it."
            )
            return redirect(self.success_url)
