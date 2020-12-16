from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import AddMessageForm
from workoutuser.models import WorkoutUser

# Create your views here.


@login_required()
def social_dashboard_view(request):
    workout_user = WorkoutUser.objects.get(username=request.user)
    workout_users = WorkoutUser.objects.all()
    messages = Message.objects.filter(
        author=request.user).order_by('-time_published')
    messages_count = Message.objects.filter(author=request.user).all().count()
    follow_count = workout_user.follow.all().count()
    return render(request, 'social.html', {
        'messages': messages,
        'messages_count': messages_count,
        'workout_users': workout_users,
        'follow_count': follow_count
    })


@login_required()
def author_detail_view(request, author_id):
    author_information = WorkoutUser.objects.get(id=author_id)
    author_messages_count = Message.objects.filter(
        author=author_information).all().count()
    follow_count = author_information.follow.all().count()
    return render(request, "author_detail.html", {
        "author": author_information,
        "author_messages_count": author_messages_count,
        'follow_count': follow_count
    })


@login_required()
def add_tweet_view(request):
    if request.method == 'POST':
        form = AddMessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Message.objects.create(
                post=data['post'],
                author=request.user
            )

            return HttpResponseRedirect(reverse('social'))

    form = AddMessageForm()
    return render(request, 'generic_form.html', {'form': form})


@login_required()
def user_follow_view(request, author_id):
    user_to_follow = WorkoutUser.objects.get(id=author_id)
    logged_in_user = WorkoutUser.objects.get(username=request.user)
    logged_in_user.follow.add(user_to_follow)
    logged_in_user.save()
    return HttpResponseRedirect(reverse('social'))


@login_required()
def user_unfollow_view(request, author_id):
    user_to_unfollow = WorkoutUser.objects.get(id=author_id)
    logged_in_user = WorkoutUser.objects.get(username=request.user)
    logged_in_user.follow.remove(user_to_unfollow)
    logged_in_user.save()
    return HttpResponseRedirect(reverse('social'))
