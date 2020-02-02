from django.shortcuts import render

from quizzy.models.quiz import Quiz


def quiz_take_all(request):
    questions = Quiz.objects.all()

    return render(request, 'quiz/quiz_take_all.html', {'questions': questions})
