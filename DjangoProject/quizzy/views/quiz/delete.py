from django.urls import reverse_lazy
from django.views.generic import DeleteView

from quizzy.models.quiz import Quiz


class QuizDeleteView(DeleteView):
    template_name = 'quiz/quiz_delete.html'
    model = Quiz
    success_url = reverse_lazy('quizzy_index')
