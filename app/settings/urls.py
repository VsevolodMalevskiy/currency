from django.contrib import admin
# from django.contrib.auth import views
from django.urls import path, include
from currency.views import IndexView, RegisterUser


urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('account/', include('account.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('', IndexView.as_view(), name='index'),
    path('currency/', include('currency.urls')),
]
