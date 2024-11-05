from django import forms
class UserForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    age = forms.IntegerField(label='Возраст')