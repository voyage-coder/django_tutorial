from django import forms

# instead of specifying fields individually in html and parsing them
# we can model them as a class
# jst like we did in fastapi models with sqla
# we can do easy validation with them

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Your Name')
    age = forms.IntegerField(label='Your Age')
    job = forms.CharField(max_length=100, required=False, label='Your Job')
