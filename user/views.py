from rest_framework import generics
from rest_framework import mixins
from .models import PlantFlixUser
from .serializers import PlantFlixUserSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User


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


class UserView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None, **kwargs):
        if request.user and pk ==1:
            return Response(UserSerializer(request.user).data)
        return super(UserView, self).retrieve(request, pk)
