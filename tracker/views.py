from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .models import Workout
from .forms import AddWorkout

# Create your views here.


@login_required()
def dashboard_view(request):
  user_workouts = Workout.objects.filter(user_created=request.user)
  return render(request, 'tracker_dashboard.html', {"user_workouts": user_workouts})


@login_required()
def add_workout_view(request):
  if request.method == 'POST':
        form = AddWorkout(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Workout.objects.create(
                title=data['title'],
                description=data['description'],
                workout_status='New',
                user_created=request.user,
            )
            return HttpResponseRedirect(reverse('tracker_dashboard'))

  form = AddWorkout()
  return render(request, 'generic_form.html', {'form': form})


@login_required()
def workout_detail_view(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  return render(request, 'workout_detail.html', {'workout': workout})


@login_required()
def new_workout_view(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  workout.workout_status = 'New'
  workout.save()
  return redirect(f'/workout_detail/{workout_id}/')


@login_required()
def in_progress_workout_view(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  workout.workout_status = 'In Progress'
  workout.save()
  return redirect(f'/workout_detail/{workout_id}/')


@login_required()
def done_workout_view(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  workout.workout_status = 'Done'
  workout.save()
  return redirect(f'/workout_detail/{workout_id}/')


@login_required()
def invalid_workout_view(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  workout.workout_status = 'Invalid'
  workout.save()
  return redirect(f'/workout_detail/{workout_id}/')
