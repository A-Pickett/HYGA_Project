from django.contrib import admin
from inventory.models import InventorySelector, InventoryItem
# Register your models here.

admin.site.register(InventorySelector)
admin.site.register(InventoryItem)

