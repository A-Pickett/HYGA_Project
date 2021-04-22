"""hygaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from inventory.views import item_create_view
from hygaproject import views

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'), #  Creating a path to redirect from the main site to a log in page
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')), #  Giving us access to djangos built in templates for login/reg/etc
    path('', include('inventory.urls')), #  Allowing us to access the inventory urls without adding inventory to the url we type in.
    path('', TemplateView.as_view(template_name='home.html'), name='home'), #  Using a class based view to access the home page. not sure why we are using a diff way of doing this
    path('create/', item_create_view) # Probably won't use this. Will probably use the UserInventory model and create a model form. (using Max Goodridge Tuturials)
]
# making an if statement so that when we are in dev (if debug is set to TRUE) we use these paths.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_URL)
