from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Messages(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.message


class Announcements(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class FounderMessage(Announcements):
    pass

    def __str__(self):
        return self.title


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()
    qualification = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    pass

    def __str__(self):
        return "HI"
