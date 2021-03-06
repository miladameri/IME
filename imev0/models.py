# This Python file uses the following encoding: utf-8
from django.db import models
from django_jalali.db import models as jmodels


class MainGroup(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name


class SubGroup(models.Model):
    name = models.CharField(max_length=255, default="")
    mainGroup = models.ForeignKey(MainGroup)

    def __str__(self):
        return self.name + '  -  '+ self.mainGroup.__str__()


class Group(models.Model):
    name = models.CharField(max_length=255, default="")
    subGroup = models.ForeignKey(SubGroup, null=True)

    def __str__(self):
        return self.name + '  -  ' + self.subGroup.__str__()


class Product(models.Model):
    name = models.CharField(max_length=255, default="")
    group = models.ForeignKey(Group)

    def __str__(self):
        return self.name + '  -  ' + self.group.__str__()


class Producer(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    date = jmodels.jDateField(verbose_name='تاریخ')
    product = models.ForeignKey(Product, verbose_name='محصول')
    producer = models.ForeignKey(Producer, verbose_name='تولیدکننده')
    supply = models.FloatField(default=-1, verbose_name='عرضه')
    demand = models.FloatField(default=-1, verbose_name='تقاضا')
    trade = models.FloatField(default=-1, verbose_name='معامله')        #moamele
    value_KRials = models.FloatField(default=-1, verbose_name='ارزش(هزارریال)')
    def __str__(self):
        return str(self.date) + ", " + str(self.product) + ", " + str(self.supply)
