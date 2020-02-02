from django.urls import reverse
from django.views.generic import CreateView

from quizzy.forms.person import PersonForm
from quizzy.models.person import Person


class PersonCreateView(CreateView):
    template_name = 'register.html'
    model = Person

    form_class = PersonForm

    def get_success_url(self):
        return reverse('quizzy_index')
