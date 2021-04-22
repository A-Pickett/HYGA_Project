from django.contrib import admin
from accounts.models import UserInventory, UserProfile
# Register your models here.

# using tutorial https://www.youtube.com/watch?v=mWNeTTDB3zQ&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=11
# around 6 mins into vid. Registering the model with the admin
admin.site.register(UserInventory)
admin.site.register(UserProfile)