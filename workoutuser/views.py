from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import WorkoutUser, UserGoals
from .forms import AddUserForm, UpdateUserForm, AddUserGoals
# Create your views here.


@login_required()
def profile_view(request):
    return render(request, 'profile.html')


@login_required()
def add_user_view(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            WorkoutUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                age=data['age'],
                height=data['height'],
                weight=data['weight'],
                fitness_level=data['fitness_level'],
            )
            return HttpResponseRedirect(reverse('login'))

    form = AddUserForm()
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

@login_required()
def user_info_view(request):
    workout_user = WorkoutUser.objects.get(username=request.user)
    return render(request, 'userinfo.html', {"workout_user": workout_user})


@login_required()
def add_goals_view(request):
    if request.method == 'POST':
        form = AddUserGoals(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_goals = UserGoals.objects.create(
                goal_one=data['goal_one'],
                goal_two=data['goal_two'],
                goal_three=data['goal_three'],
                goal_four=data['goal_four'],
                goal_five=data['goal_five'],
                workout_user=request.user
            )
            return HttpResponseRedirect(reverse('profile'))

    form = AddUserGoals()
    return render(request, 'generic_form.html', {'form': form})
