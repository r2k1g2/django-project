from django.views.generic import ListView

from quizzy.models.person import Person


class PersonList(ListView):
    template_name = 'person/person_list.html'
    model = Person

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Tous les utilisateurs'

        #  Model . objects . la requete car c'est objects qui s'occupe de faire la requete SQL
        result['persons'] = Person.objects.all()

        return result
