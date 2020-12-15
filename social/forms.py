from django import forms

class AddMessageForm(forms.Form):
    post = forms.CharField(max_length=150)
