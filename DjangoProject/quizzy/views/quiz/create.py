from django.urls import reverse
from django.views.generic import CreateView

from quizzy.forms.quiz import QuizForm
from quizzy.models.quiz import Quiz


class QuizCreateView(CreateView):
    template_name = 'quiz/quiz_create.html'
    model = Quiz

    form_class = QuizForm

    def get_success_url(self):
        return reverse('quizzy_index')
