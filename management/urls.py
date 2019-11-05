from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"message", MessagesViewSet)
router.register(r"announcement", AnnouncementsViewSet)
router.register(r"fmessage", FounderMessageViewSet)
router.register(r"contact", ContactUsViewSet)
router.register(r"faculty", FacultyViewSet)

urlpatterns = [
    path("", include(router.urls))
]
