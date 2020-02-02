from django.views.generic import ListView

from quizzy.models.quiz import Quiz


class QuizListView(ListView):
    template_name = 'quiz/quiz_list.html'
    model = Quiz

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['question'] = 'Tous les quizzes'

        result['quizzes'] = Quiz.objects.all()

        return result
