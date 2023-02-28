"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from currency.views import (
    list_rates, list_contact_us,
    rates_create, list_rates_7,
    request_methods, rates_update,
    rates_delete, rates_details,
    list_source, source_create,
    source_update, source_delete,
    source_details, source_table,
    start_page
)


urlpatterns = [
    path('', start_page),
    path('admin/', admin.site.urls),
    path('rate/list/', list_rates),
    path('rate/list_7/', list_rates_7),
    path('rate/create/', rates_create),
    path('rate/details/<int:pk>/', rates_details),
    path('rate/update/<int:pk>/', rates_update),
    path('rate/delete/<int:pk>/', rates_delete),
    path('contact_us/list/', list_contact_us),
    path('rm/', request_methods),
    path('source/list/', list_source),
    path('source/create/', source_create),
    path('source/details/<int:pk>/', source_details),
    path('source/update/<int:pk>/', source_update),
    path('source/delete/<int:pk>/', source_delete),
    path('source/table/', source_table),

]
