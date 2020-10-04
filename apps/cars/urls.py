from django.urls import path, include
from rest_framework import routers
from .api import CarCreateApi, CarApi, CarUpdateApi, CarDeleteApi

urlpatterns = [
    path('',CarApi.as_view()),
    path('create',CarCreateApi.as_view()),
    path('update/<int:pk>',CarUpdateApi.as_view()),
    path('delete/<int:pk>',CarDeleteApi.as_view()),
]

# urlpatterns = [
#     path('hello', SimpleApI.as_view()),
# ]