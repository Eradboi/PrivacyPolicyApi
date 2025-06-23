# DJANGO IMPORTS
from django.contrib import admin
from django.urls import path

# VIEWS IMPORTS
from .views import privacy_policy, terms_and_condition


urlpatterns = [
    path('privacy-policy/',privacy_policy,name='privacy-policy'),
    path('terms-and-conditions/',terms_and_condition,name='terms-and-conditions')
]