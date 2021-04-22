from django.shortcuts import render, get_object_or_404
from inventory.models import InventorySelector, InventoryItem
# Importing the CreateView to allow us to use forms to create new objects
from django.views.generic.edit import CreateView
from inventory.forms import ItemCreateForm


# Create your views here.

#  Creating a CreateView subclass to allow the users to create an InventoryItem object
#  (we choose which fields they can input)
def item_create_view(request):
    form = ItemCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ItemCreateForm()

    context = {
        'form': form
     }
    return render(request, "inventory/item_create.html", context)

# This view uses a raw form, not a model form to collect the data. We're only using this to learn
#  how forms work. I'll delete this when not needed.
# def item_create_view(request):
#     my_form = RawItemCreateForm()
#     if request.method == "POST":
#         my_form = RawItemCreateForm(request.POST)
#         #  Checking if the data has been entered as required
#         if my_form.is_valid():
#             #  now the data is good
#             print(my_form.cleaned_data)
#             InventoryItem.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "inventory/item_create.html", context)


def inventory_index(request):
    options = InventorySelector.objects.all()
    return render(request, 'inventory/index.html',
                  {'options': options})


def my_inventory(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/myinventory.html',
                  {'items': items})


def item_detail(request, pk):
    item = InventoryItem.objects.get(pk=pk)
    return render(request, 'inventory/item_detail.html',
                  {'item': item})


def home(request):
    return render(request, 'home.html')
