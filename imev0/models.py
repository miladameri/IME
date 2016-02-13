# This Python file uses the following encoding: utf-8
from django.db import models


class MainGroup(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255, default="")
    mainGroup = models.ForeignKey(MainGroup)

    def __str__(self):
        return self.name + ' در ' + self.mainGroup.__str__()


class Product(models.Model):
    name = models.CharField(max_length=255, default="")
    group = models.ForeignKey(Group)

    def __str__(self):
        return self.name + ' در ' + self.group.__str__()


class Producer(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    date = models.DateField()
    product = models.ForeignKey(Product)
    producer = models.ForeignKey(Producer)
    supply = models.FloatField(default=0)
    demand = models.FloatField(default=0)
    value_KRials = models.FloatField(default=0)
    treatment = models.FloatField(default=0)
