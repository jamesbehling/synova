from django.db import models
from employees.models import Employee
from houses.models import House


class EmployeeAssignment(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE
    )

    start_date = models.DateField()

    end_date = models.DateField(
        null=True,
        blank=True
    )

    primary_assignment = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.employee} -> {self.house}"
