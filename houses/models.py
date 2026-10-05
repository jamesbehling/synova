from django.db import models
from employees.models import Employee


class House(models.Model):

    name = models.CharField(
        max_length=100
    )

    address = models.CharField(
        max_length=255
    )

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=50
    )

    zipcode = models.CharField(
        max_length=10
    )

    bedrooms = models.IntegerField(
        default=0
    )

    bathrooms = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0
    )

    capacity = models.IntegerField(
        default=0
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


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
