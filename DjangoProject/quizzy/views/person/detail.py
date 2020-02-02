from django.views.generic import DetailView

from quizzy.models.person import Person


class PersonDetailView(DetailView):
    template_name = 'person/person_detail.html'
    model = Person
