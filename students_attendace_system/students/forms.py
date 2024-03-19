from django import forms


class StudentForm(forms.Form):
    firstname = forms.CharField(label="firstname", max_length=100)