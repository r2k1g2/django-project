from django.forms import models

from quizzy.models.person import Person


class PersonForm(models.ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
