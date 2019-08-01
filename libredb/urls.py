from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<str:app_name>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<str:app_name>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<str:app_name>/vote/', views.vote, name='vote'),
]
