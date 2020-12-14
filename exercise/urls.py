"""exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from authentication.views import login_view, logout_view
from workoutuser.views import profile_view, add_user_profile_view, update_profile_view, update_goals_view, add_todo_view, update_todo_view, remove_todo_view
from tracker.views import dashboard_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view),
    path('profile/', profile_view, name='profile'),
    path('add_user/', add_user_profile_view, name='add_user'),
    path('update_user/', update_profile_view, name='update_user'),
    path('update_goals/', update_goals_view, name='update_goals'),
    path('add_todos/', add_todo_view, name='add_todos'),
    path('update_todos/<int:todo_id>/', update_todo_view, name='update_todos'),
    path('remove_todo/<int:todo_id>/', remove_todo_view, name='remove_todo'),
    path('tracker_dashboard/', dashboard_view, name='tracker_dashboard'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
