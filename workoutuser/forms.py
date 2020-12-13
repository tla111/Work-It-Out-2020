from django import forms
from .models import WorkoutUser


class AddUserProfileForm(forms.Form):
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

    goal_one = forms.CharField(max_length=200)
    goal_two = forms.CharField(max_length=200)
    goal_three = forms.CharField(max_length=200)
    goal_four = forms.CharField(max_length=200)
    goal_five = forms.CharField(max_length=200)


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = WorkoutUser
        fields = ['age', 'height', 'weight', 'fitness_level']


class UpdateGoalsForm(forms.ModelForm):
    class Meta:
        model = WorkoutUser
        fields = ['goal_one', 'goal_two',
                  'goal_three', 'goal_four', 'goal_five']
