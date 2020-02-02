from django import forms
from django.forms import models

from quizzy.models.quiz import Quiz


class QuizForm(models.ModelForm):
    answer = forms.CharField(max_length=1, help_text="for example : 'a' for the option 1, 'b' for the option 2")

    class Meta:
        model = Quiz
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer']
