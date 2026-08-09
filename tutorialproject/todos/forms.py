from django import forms
from .models import Todo

# instead of specifying fields individually in html and parsing them
# we can model them as a class
# jst like we did in fastapi models with sqla
# we can do easy validation with them

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Your Name')
    age = forms.IntegerField(label='Your Age')
    job = forms.CharField(max_length=100, required=False, label='Your Job')


class TodoForm(forms.ModelForm):
    # this ModelForm have an advantage
    # we jst need to specify the model and it will generate form based on that
    class Meta:
        model = Todo
        fields = ['title', 'description', 'done', 'deadline', 'priority']
        # we can also customize widgets here
        # for example if we dont want plain text text in deadline but a date picker
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }