from django.views.generic import DetailView

from quizzy.models.quiz import Quiz


class QuizDetailView(DetailView):
    template_name = 'quiz/quiz_detail.html'
    model = Quiz
