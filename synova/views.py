from django.shortcuts import render

from employees.models import Employee
from houses.models import House


def home(request):

    context = {
        'employee_count':
            Employee.objects.count(),

        'house_count':
            House.objects.count(),
    }

    return render(
        request,
        'home.html',
        context
    )
