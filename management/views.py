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


class AnnouncementsViewSet(ReadOnlyModelViewSet):
    queryset = Announcements.objects.all()
    serializer_class = Announcements
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FounderMessageViewSet(ReadOnlyModelViewSet):
    queryset = FounderMessage.objects.all()
    serializer_class = FounderMessage
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ContactUsViewSet(ReadOnlyModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUs
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
