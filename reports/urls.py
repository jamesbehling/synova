from django.urls import path
from .views import HouseEmployeeReportView

app_name = 'reports'

urlpatterns = [
    path('houses-employees/', HouseEmployeeReportView.as_view(), name='house_employee_report'),
]
