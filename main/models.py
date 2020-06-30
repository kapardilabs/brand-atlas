from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Country(models.Model):
    name = models.CharField(max_length=500)
    flag_icon = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=1000)
    origin_country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=1500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.URLField(max_length=10000, null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    edited = models.BooleanField(default=False)
    finalise = models.BooleanField(default=False)

    class Meta:
        unique_together = ("name", "origin_country")

    def __str__(self):
        return str(self.name) + " <-> " + str(self.origin_country)


class Messages(models.Model):
    sender = models.CharField(max_length=150)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.sender)
