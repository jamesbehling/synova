from django.views.generic import ListView
from django.db.models import Count
from houses.models import House

app_name = 'reports'

class HouseEmployeeReportView(ListView):
    model = House
    template_name = 'reports/house_employee_report.html'
    context_object_name = 'houses'

    def get_queryset(self):
        # Annotate each house with the count of its assigned employees via employeeassignment
        return House.objects.annotate(employee_count=Count('employeeassignment'))
