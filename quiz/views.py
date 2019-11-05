from rest_framework import generics
from rest_framework import mixins
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


#
# class QuestionList(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class QuizViewSet(ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if request.user:
            queryset = Quiz.objects.filter(users__in=[request.user])
            return Response(QuizSerializer(queryset, many=True).data)
        else:
            queryset = Quiz.objects.filter(id=-1)
            return Response(QuizSerializer(queryset, many=True).data)


class UserAnswerViewSet(ReadOnlyModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = [IsAuthenticated]


class QuestionViewSet(ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
