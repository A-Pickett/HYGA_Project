from django.urls import path
from inventory import views

app_name = 'inventory'

urlpatterns = [
    path('inventory/', views.inventory_index, name="inventory_index"),
    path('myinventory/', views.my_inventory, name="my_inventory"),
    path("myinventory/<int:pk>", views.item_detail, name="item_detail"),
    path('home/', views.home, name="home"),
]
