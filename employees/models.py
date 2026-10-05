from django.db import models


class Title(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Employee(models.Model):

    prefix = models.CharField(
        max_length=20,
        blank=True
    )

    first_name = models.CharField(
        max_length=100
    )

    middle_name = models.CharField(
        max_length=100,
        blank=True
    )

    last_name = models.CharField(
        max_length=100
    )

    suffix = models.CharField(
        max_length=20,
        blank=True
    )

    title = models.ForeignKey(
        Title,
        on_delete=models.PROTECT
    )

    manager = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subordinates'
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=25,
        blank=True
    )

    hire_date = models.DateField(
        null=True,
        blank=True
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
