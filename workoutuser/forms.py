from django import forms
from .models import WorkoutUser


class AddUserForm(forms.Form):
    FITNESS = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )

    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.CharField(max_length=2)
    height = forms.CharField(max_length=3)
    weight = forms.CharField(max_length=3)
    fitness_level = forms.ChoiceField(choices=FITNESS)
