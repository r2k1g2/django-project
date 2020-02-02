from django.views.generic import ListView

from quizzy.models.quiz import Quiz


class IndexView(ListView):
    template_name = 'index.html'
    model = Quiz

    # Method qui remplie le saut de variable ; va chercher la méthode parente
    # Dictionnaire qui contient toutes les valeurs qu'on va envoyer dans data
    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['question'] = 'Tous les quizzes'

        result['quiz'] = Quiz.objects.all()

        return result

    # On peut faire get_query_set qui renvoi une liste d'objets si on veut faire sa propre requete du coup ici elle
    # contiendrait Cocktail.objects.all()
