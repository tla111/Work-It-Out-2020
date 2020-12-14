from django.db import models
from django.utils import timezone
from workoutuser.models import WorkoutUser


# Create your models here.

class Workout(models.Model):
    STATUS = (
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid')
    )

    title = models.CharField(max_length=200)
    date_filed = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    workout_status = models.CharField(max_length=200, choices=STATUS)
    user_created = models.ForeignKey(WorkoutUser, on_delete=models.CASCADE,
                                     related_name="created_by_workoutuser", blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.title}"
