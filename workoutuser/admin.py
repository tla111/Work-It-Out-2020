from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import WorkoutUser, Todos

# Register your models here.


admin.site.register(WorkoutUser, UserAdmin)
admin.site.register(Todos)

