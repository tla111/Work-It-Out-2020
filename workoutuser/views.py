from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import WorkoutUser
from .forms import AddUserProfileForm, UpdateUserForm, UpdateGoalsForm
# Create your views here.


@login_required()
def profile_view(request):
    goals = WorkoutUser.objects.get(username=request.user)
    return render(request, 'profile.html', {'goals': goals})


@login_required()
def add_user_profile_view(request):
    if request.method == 'POST':
        form = AddUserProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            WorkoutUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                age=data['age'],
                height=data['height'],
                weight=data['weight'],
                fitness_level=data['fitness_level'],
                goal_one=data['goal_one'],
                goal_two=data['goal_two'],
                goal_three=data['goal_three'],
                goal_four=data['goal_four'],
                goal_five=data['goal_five'],
            )
            return HttpResponseRedirect(reverse('login'))

    form = AddUserProfileForm()
    return render(request, 'generic_form.html', {'form': form})


def update_profile_view(request):
    instance = WorkoutUser.objects.get(username=request.user)
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("profile"))

    form = UpdateUserForm(instance=instance)
    return render(request, 'generic_form.html', {'form': form})


def update_goals_view(request):
    instance = WorkoutUser.objects.get(username=request.user)
    if request.method == "POST":
        form = UpdateGoalsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("profile"))

    form = UpdateGoalsForm(instance=instance)
    return render(request, 'generic_form.html', {'form': form})
