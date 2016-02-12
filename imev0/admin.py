from django.contrib import admin

# Register your models here.
from imev0.models import Transaction

class TAdmin(admin.ModelAdmin):
    list_display = ('date', 'product', 'producer', 'supply')


admin.site.register(Transaction, TAdmin)
