from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class WorkoutUser(AbstractUser):
  FITNESS= (
       ('Beginner', 'Beginner'),
       ('Intermediate', 'Intermediate'),
       ('Advanced', 'Advanced'),
   )
  
  display_name = models.CharField(
      max_length=200, blank=True, null=True, default=None)
  age = models.CharField(max_length=2, blank=True, null=True, default=None)
  height = models.CharField(max_length=2, blank=True, null=True, default=None)
  weight = models.CharField(max_length=3, blank=True, null=True, default=None)
  fitness_level = models.CharField(
      max_length=200, choices=FITNESS, blank=True, null=True, default=None)

  def __str__(self):
    return f"{self.username}"


class UserGoals(models.Model):
    workout_user = models.ForeignKey(
        WorkoutUser, on_delete=models.CASCADE, null=True)
    goal_one = models.CharField(max_length=200)
    goal_two = models.CharField(max_length=200)
    goal_three = models.CharField(max_length=200)
    goal_four = models.CharField(max_length=200)
    goal_five = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.goal_one}"
