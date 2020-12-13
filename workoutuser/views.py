from django.shortcuts import render, reverse, HttpResponseRedirect

from .models import WorkoutUser
from .forms import AddUserForm
# Create your views here.

def profile_view(request):
    return render(request, 'profile.html')

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
            return HttpResponseRedirect(reverse('profile'))

    form = AddUserForm()
    return render(request, 'generic_form.html', {'form': form})


def user_info_view(request):
    workout_user = WorkoutUser.objects.get(username=request.user)
    return render(request, 'userinfo.html', {"workout_user": workout_user})
