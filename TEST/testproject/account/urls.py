from . import views
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('account/api/', views.CustomLoginView.as_view(), name='account'),
]
