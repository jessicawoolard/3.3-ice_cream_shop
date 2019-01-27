from django.db import models


class IceCream(models.Model):
    flavor = models.CharField(max_length=100)
    base = models.CharField(max_length=100)
    available = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)
    churned = models.DateField()
