from django.db import models
from django.contrib.auth.models import User
from course.models import Course
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mobile = models.IntegerField(blank=True, null=True)
    profile_photo = models.ImageField(blank=True, null=True)
    courses = models.ManyToManyField(Course, blank=True, null=True)

    def __str__(self):
        return self.name


def save_profile(sender, instance, **kwargs):
    print(instance.id)
    try:
       UserAccount.objects.get(user=instance)
    except UserAccount.DoesNotExist:
        user = UserAccount(
            user=instance,
            name=str(instance),
        )
        user.save()


post_save.connect(save_profile, sender=User)
