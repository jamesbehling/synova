from django.db import models
from employees.models import Employee

class Car(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    vin = models.CharField(max_length=17, unique=True, verbose_name="VIN Number")
    color = models.CharField(max_length=30)
    assigned_employee = models.ForeignKey(
        Employee, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='assigned_cars'
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.vin[-6:]})"

class CarMaintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='maintenance_logs')
    date = models.DateField()
    mileage = models.PositiveIntegerField()
    description = models.TextField(verbose_name="Service Reason / Work Done")
    breakfix = models.BooleanField(default=False,verbose_name="Break-fix (Major Repair vs. Routine Maintenance)")

    def __str__(self):
        service_type = "Repair" if self.breakfix else "Routine"
        return f"{service_type} for {self.car} on {self.date} at {self.mileage} miles"
