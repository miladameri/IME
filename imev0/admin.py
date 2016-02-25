# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from imev0.models import *


class TAdmin(admin.ModelAdmin):
    list_display = ('persian_date', 'product', 'producer', 'supply', 'demand', 'trade', 'value_KRials')

    def persian_date(self, obj):
        day = str(obj.date.day)
        year = str(obj.date.year)
        persian = {'0':'۰','1':'۱','2':'۲','3':'۳','4':'۴','5':'۵','6':'۶','7':'۷','8':'۸','9':'۹', '/':'/'}
        new_year = ''.join(persian.get(ch, ch) for ch in year)
        new_day = ''.join(persian.get(ch, ch) for ch in day)
        months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
        new_month = months[obj.date.month]
        return "روز " + new_day + " " + new_month + " " + new_year
    persian_date.short_description = "تاریخ"

admin.site.register(Transaction, TAdmin)


class PAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, PAdmin)
admin.site.register(Producer, PAdmin)
admin.site.register(Group, PAdmin)
admin.site.register(MainGroup, PAdmin)
admin.site.register(SubGroup, PAdmin)
