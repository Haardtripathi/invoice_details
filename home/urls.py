from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('invoices/',get_detailsAPI.as_view())
]
