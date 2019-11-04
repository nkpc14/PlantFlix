from django.urls import path
from .views import *

urlpatterns = [
    path('', PlantFlixUserList.as_view(), name='users-list'),
    path('signup', PlantFlixUserCreate.as_view(), name='users-list'),
]
