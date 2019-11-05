from rest_framework import generics
from rest_framework import mixins
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


class MessagesViewSet(ReadOnlyModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if request.user:
            queryset = Messages.objects.filter(users__in=[request.user])
            return Response(MessagesSerializer(queryset, many=True).data)
        else:
            queryset = Messages.objects.filter(id=-1)
            return Response(MessagesSerializer(queryset, many=True).data)


class AnnouncementsViewSet(ReadOnlyModelViewSet):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FounderMessageViewSet(ReadOnlyModelViewSet):
    queryset = FounderMessage.objects.all()
    serializer_class = FounderMessageSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FacultyViewSet(ReadOnlyModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated]

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)


class ContactUsViewSet(ReadOnlyModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUs
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
