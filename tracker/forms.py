from django import forms
from .models import Workout


class AddWorkout(forms.Form):
  title = forms.CharField(max_length=200)
  description = forms.CharField(widget=forms.Textarea)
