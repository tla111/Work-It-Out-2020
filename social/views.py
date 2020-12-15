from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from workoutuser.models import WorkoutUser

# Create your views here.


@login_required()
def social_dashboard_view(request):
    # logged_in_user = WorkoutUser.objects.get(username=request.user)
    messages = Message.objects.filter(author=request.user)
    return render(request, 'social.html', {'messages': messages})



  
