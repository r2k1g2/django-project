"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_quizzy import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_quizzy.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path

from quizzy.views.login import LoginView
from quizzy.views.index import IndexView
from quizzy.views.logout import LogoutView
from quizzy.views.person.detail import PersonDetailView
from quizzy.views.person.list import PersonList
from quizzy.views.quiz.create import QuizCreateView
from quizzy.views.quiz.delete import QuizDeleteView
from quizzy.views.quiz.detail import QuizDetailView
from quizzy.views.quiz.list import QuizListView
from quizzy.views.quiz.take_all_quiz import quiz_take_all
from quizzy.views.quiz.take_quiz import quiz_take
from quizzy.views.quiz.update import QuizUpdateView
from quizzy.views.signup import sign_up_view

urlpatterns = [


]

urlpatterns += i18n_patterns(

    path('admin/', admin.site.urls),

    url(r'^$', IndexView.as_view(), name='quizzy_index'),

    path('quiz/list',
         QuizListView.as_view(),
         name='quizzy_quiz_list'),

    path('quiz/detail/<int:pk>',
         QuizDetailView.as_view(),
         name='quizzy_quiz_detail'),

    path('quiz/create',
         QuizCreateView.as_view(),
         name='quizzy_quiz_create'),

    path('quiz/update/<int:pk>',
         QuizUpdateView.as_view(),
         name='quizzy_quiz_update'),

    path('quiz/delete/<int:pk>',
         QuizDeleteView.as_view(),
         name='quizzy_quiz_delete'),

    path('persons/list',
         PersonList.as_view(),
         name='quizzy_person_list'),

    path('persons/detail/<int:pk>',
         PersonDetailView.as_view(),
         name='quizzy_person_detail'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    path('quiz/take/<int:pk>/', quiz_take, name='quizzy_quiz_take'),
    path('quiz/take/all/', quiz_take_all, name='quizzy_quiz_take_all'),

    url('signup/', sign_up_view, name='signup'),

)

