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
from workoutuser.views import profile_view, add_user_view, user_info_view, update_profile_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view),
    path('profile/', profile_view, name='profile'),
    path('user_info/', user_info_view, name='user_info'),
    path('update_user/', update_profile_view, name='update_user'),
    path('adduser/', add_user_view, name='adduser'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
