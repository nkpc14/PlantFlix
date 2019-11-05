from rest_framework import serializers
from .models import *


class PlantFlixUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantFlixUser
        fields = [
            'name',
            'email',
            'password',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]
