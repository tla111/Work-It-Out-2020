from django.db import models
from django.utils import timezone
from workoutuser.models import WorkoutUser

# Create your models here.


class Message(models.Model):
    author = models.ForeignKey(WorkoutUser, on_delete=models.CASCADE)
    post = models.CharField(max_length=150)
    time_published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.post}"
