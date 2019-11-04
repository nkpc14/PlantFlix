from django.urls import include, path
from .views import QuestionViewSet, UserAnswerViewSet
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"answer", UserAnswerViewSet)
router.register(r"question", QuestionViewSet)
router.register(r"quiz", QuizViewSet)

urlpatterns = [
    path("", include(router.urls))
]
