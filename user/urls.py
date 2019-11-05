from django.urls import path
from .views import *

urlpatterns = [
    path('', PlantFlixUserList.as_view(), name='users-list'),
    # path('get/<int:pk>', UserView.as_view(), name='users-list'),
    # path('signup', PlantFlixUserCreate.as_view(), name='users-list'),
]
