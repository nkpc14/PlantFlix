from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=5000)
    optionA = models.CharField(max_length=255)
    optionB = models.CharField(max_length=255)
    optionC = models.CharField(max_length=255)
    optionD = models.CharField(max_length=255)
    correctOption = models.IntegerField(choices=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    ))

    def __str__(self):
        return self.question


class Quiz(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class UserAnswer(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=10)

    def __str__(self):
        return str(self.question) + '--' + self.answer
