from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    flag_icon = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class CrawlConfig(models.Model):
    url = models.TextField(max_length=15000)
    brand_selector = models.CharField(max_length=100)
    country_selector = models.CharField(max_length=100, null=True, blank=True)
    description_selector = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crawled = models.BooleanField(default=False)
    user_agent = models.CharField(max_length=10000, null=True, blank=True,
                                  default="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 "
                                          "Firefox/78.0")

    def __str__(self):
        return str(self.user) + "'s crawl config"


class Brand(models.Model):
    name = models.CharField(max_length=500)
    origin_country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=1500, blank=True, null=True)

    def __str__(self):
        return str(self.name) + " <-> " + str(self.origin_country)
