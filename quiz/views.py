from rest_framework import generics
from rest_framework import mixins
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import *
from rest_framework.generics import UpdateAPIView


#
# class QuestionList(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class QuizViewSet(ReadOnlyModelViewSet, generics.GenericAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        if request.user:
            queryset = Quiz.objects.filter(users__in=[request.user])
            return Response(QuizSerializer(queryset, many=True).data)
        else:
            queryset = Quiz.objects.filter(id=-1)
            return Response(QuizSerializer(queryset, many=True).data)


class QuizUpdateAPIView(UpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserAnswerViewSet(ReadOnlyModelViewSet, generics.CreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['users'] = request.user
        # print(serializer.validated_data['question'])
        # answer = get_object_or_404(UserAnswer, users=request.user, question=serializer.validated_data.get('question'))
        try:
            answer = UserAnswer.objects.get(users=request.user, question=serializer.validated_data.get('question'))
            if answer:
                answer.answer = serializer.validated_data.get('answer')
                answer.save()
                print(answer)
        except UserAnswer.DoesNotExist:
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class QuestionViewSet(ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
