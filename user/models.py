from django.db import models
from django.contrib.auth.models import User
from course.models import Course


# Create your models here.

class PlantFlixUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mobile = models.IntegerField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
