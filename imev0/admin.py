from django.contrib import admin

# Register your models here.
from imev0.models import *


class TAdmin(admin.ModelAdmin):
    list_display = ('date', 'product', 'producer', 'supply', 'demand', 'trade', 'value_KRials')

admin.site.register(Transaction, TAdmin)


class PAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, PAdmin)
admin.site.register(Producer, PAdmin)
admin.site.register(Group, PAdmin)
admin.site.register(MainGroup, PAdmin)
