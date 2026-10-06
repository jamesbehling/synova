from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy

from .models import Employee


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/list.html'


class EmployeeCreateView(CreateView):
    model = Employee

    fields = [
        'prefix',
        'first_name',
        'middle_name',
        'last_name',
        'suffix',
        'title',
        'manager',
        'email',
        'phone',
        'hire_date',
        'terminated_date',
        'active',
    ]

    template_name = 'employees/form.html'

    success_url = reverse_lazy(
        'employee_list'
    )


class EmployeeUpdateView(UpdateView):
    model = Employee

    fields = [
        'prefix',
        'first_name',
        'middle_name',
        'last_name',
        'suffix',
        'title',
        'manager',
        'email',
        'phone',
        'hire_date',
        'terminated_date',
        'active',
    ]

    template_name = 'employees/form.html'

    success_url = reverse_lazy(
        'employee_list'
    )


class EmployeeDeleteView(DeleteView):
    model = Employee

    template_name = 'employees/delete.html'

    success_url = reverse_lazy(
        'employee_list'
    )
