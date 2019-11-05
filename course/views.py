from rest_framework import generics
from rest_framework import mixins
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


class VideoViewSet(ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]


class CourseViewSet(ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if request.user:
            queryset = Course.objects.filter(users__in=[request.user])
            return Response(CourseSerializer(queryset, many=True).data)
        else:
            queryset = Course.objects.filter(id=-1)
            return Response(CourseSerializer(queryset, many=True).data)
