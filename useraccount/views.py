from rest_framework import generics
from rest_framework import mixins
from .models import UserAccount
from .serializers import PlantFlixUserSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User


class PlantFlixUserList(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = PlantFlixUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = UserAccount.objects.get(pk=request.user.id)
        print(user.id)
        serializer = PlantFlixUserSerializer(user)
        return Response( serializer.data)


class PlantFlixUserCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = PlantFlixUserSerializer

    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None, **kwargs):
        if request.user:
            return Response(UserSerializer(request.user).data)
        return super(UserView, self).retrieve(request, pk)
