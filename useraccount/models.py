from django.db import models
from django.contrib.auth.models import User
from course.models import Course
from django.db.models import signals


# Create your models here.

class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mobile = models.IntegerField()
    profile_photo = models.ImageField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

#     def create_profile(sender, instance, created, **kwargs):
#         user = UserAccount(instance)
#
# signals.post_save.connect(receiver=create_profile, sender=User)
