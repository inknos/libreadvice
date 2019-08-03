from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /libredb/app/Firefox/
    path('app/<str:app_name>/', views.detail, name='detail'),
    # ex: /libredb/Firefox/results/
    #path('<str:app_name>/results/', views.results, name='results'),
    # ex: /libredb/Firefox/vote/
    #path('<str:app_name>/vote/', views.vote, name='vote'),
    # ex: /libredb/app
    path('app', views.insert_application, name='insert_application')
]
