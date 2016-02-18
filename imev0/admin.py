from django.contrib import admin

# Register your models here.
from imev0.models import *


class TAdmin(admin.ModelAdmin):
    list_display = ('persian_date', 'product', 'producer', 'supply', 'demand', 'trade', 'value_KRials')

    def persian_date(self, args*):
        return "sag"

admin.site.register(Transaction, TAdmin)


class PAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, PAdmin)
admin.site.register(Producer, PAdmin)
admin.site.register(Group, PAdmin)
admin.site.register(MainGroup, PAdmin)
admin.site.register(SubGroup, PAdmin)
