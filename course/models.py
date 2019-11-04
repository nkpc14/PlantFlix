from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=255)
    pdf = models.FileField(blank=True)
    video = models.FileField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    videos = models.ManyToManyField(Video)
    about = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
