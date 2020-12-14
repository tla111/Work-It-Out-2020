from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .models import Workout

# Create your views here.


@login_required()
def dashboard_view(request):
  user_workouts = Workout.objects.filter(user_created=request.user)
  return render(request, 'tracker_dashboard.html', {"user_workouts": user_workouts})
