from django.contrib.auth import logout
from django.shortcuts import render
from django.views.generic import TemplateView


class LogoutView(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        logout(request)

        return render(request, self.template_name)
