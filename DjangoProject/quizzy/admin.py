from django.contrib import admin

# Register your models here.
from quizzy.models.person import Person
from quizzy.models.quiz import Quiz

admin.site.register(Person)
admin.site.register(Quiz)

