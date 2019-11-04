from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"course", CourseViewSet)
router.register(r"videos", VideoViewSet)

urlpatterns = [
    path("", include(router.urls))
]
