from django.contrib import admin
from .models import Hut, Address

class AddressInLine(admin.StackedInline):
    model = Address
    extra = 1

class HutAdmin(admin.ModelAdmin):
    inlines = [AddressInLine]

# Register your models here.
admin.site.register(Hut, HutAdmin)

