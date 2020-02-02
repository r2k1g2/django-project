from django.urls import reverse
from django.views.generic import UpdateView

from quizzy.forms.quiz import QuizForm
from quizzy.models.quiz import Quiz


class QuizUpdateView(UpdateView):
    template_name = 'quiz/quiz_update.html'
    model = Quiz
    form_class = QuizForm

    def get_success_url(self):
        return reverse('quizzy_index')
