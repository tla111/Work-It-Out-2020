from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import WorkoutUser

# Register your models here.


admin.site.register(WorkoutUser, UserAdmin)

