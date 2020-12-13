from django import forms
from .models import WorkoutUser, Todos


class AddUserProfileForm(forms.Form):
    FITNESS = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )

    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
    age = forms.CharField(max_length=2, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '30'
        }
    ))
    height = forms.CharField(max_length=3, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '72'
        }
    ))
    weight = forms.CharField(max_length=3, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '150'
        }
    ))
    fitness_level = forms.ChoiceField(choices=FITNESS)

    goal_one = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Run 5x a Week'
        }
    ))

    goal_two = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Workout 4x a Week'
        }
    ))

    goal_three = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Eat 3 Meals Daily'
        }
    ))

    goal_four = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Drink More Water'
        }
    ))

    goal_five = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Swim 3x a Week'
        }
    ))


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = WorkoutUser
        fields = ['age', 'height', 'weight', 'fitness_level']


class UpdateGoalsForm(forms.ModelForm):
    class Meta:
        model = WorkoutUser
        fields = ['goal_one', 'goal_two',
                  'goal_three', 'goal_four', 'goal_five']


class AddTodosForm(forms.Form):
    title = forms.CharField(max_length=200)


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['title']
