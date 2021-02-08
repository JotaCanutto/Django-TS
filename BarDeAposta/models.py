from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.name


class Customer(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    cpf_number = models.CharField(max_length=11, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=13, null=True, blank=True, unique=True)

    def __str__(self):
        return self.full_name
