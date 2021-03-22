from django.shortcuts import render
from inventory.models import InventorySelector, MyInventory

# Create your views here.


def inventory_index(request):
    options = InventorySelector.objects.all()
    return render(request, 'inventory/index.html',
                  {'options': options})


def my_inventory(request):
    items = MyInventory.objects.all()
    return render(request, 'inventory/myinventory.html',
                  {'items': items})


def item_detail(request, pk):
    item = MyInventory.objects.get(pk=pk)
    return render(request, 'inventory/item_detail.html',
                  {'item': item})


def home(request):
    return render(request, 'inventory/home.html')
