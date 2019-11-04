from rest_framework import generics
from rest_framework import mixins
from .models import PlantFlixUser
from .serializers import PlantFlixUserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


class PlantFlixUserList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = PlantFlixUser.objects.all()
    serializer_class = PlantFlixUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PlantFlixUserCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = PlantFlixUser.objects.all()
    serializer_class = PlantFlixUserSerializer

    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
