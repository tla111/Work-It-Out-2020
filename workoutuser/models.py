from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class WorkoutUser(AbstractUser):
  display_name = models.CharField(max_length=200)

  def __str__(self):
      return f"{self.username}"
