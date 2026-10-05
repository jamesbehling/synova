from django.shortcuts import render
from employees.models import Employee

def employee_report(request):
    employees = Employee.objects.all()\

    return render(
        request,
        'reports/employees.html',
        {'employees': employees}
    )

from houses.models import House

def employees_by_house(request):

    houses = House.objects.prefetch_related(
        'employeeassignment_set'
    )

    return render(
        request,
        'reports/employees_by_house.html',
        {
            'houses': houses
        }
    )

def manager_report(request):

    managers = Employee.objects.filter(
        subordinates__isnull=False
    ).distinct()

    return render(
        request,
        'reports/managers.html',
        {
            'managers': managers
        }
    )
