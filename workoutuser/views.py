from django.shortcuts import render, reverse, HttpResponseRedirect

from .models import WorkoutUser
# Create your views here.


def index_view(request):
    name = 'Tim'
    return render(request, 'index.html', {'name': name})
