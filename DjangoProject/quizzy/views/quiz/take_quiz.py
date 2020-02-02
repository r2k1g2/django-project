from django.shortcuts import render

from quizzy.models.quiz import Quiz


def quiz_take(request, pk):
    question = Quiz.objects.get(pk=pk)

    return render(request, 'quiz/quiz_take.html', {'question': question})
