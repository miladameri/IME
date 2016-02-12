from django.db import models


class Transaction(models.Model):
    date = models.DateField(null=True)
    product = models.CharField(max_length=200, default="-")
    producer = models.CharField(max_length=200, default="-")
    supply = models.FloatField(default=0)
    demand = models.FloatField(default=0)
    value_KRials = models.FloatField(default=0)
    main_group = models.CharField(max_length=200, default="-")
    group = models.CharField(max_length=200, default="-")
    sub_group = models.CharField(max_length=200, default="-")
    treatment = models.FloatField(default=0)
