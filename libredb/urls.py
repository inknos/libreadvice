from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'applications', views.ApplicationViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'pills', views.PillViewSet)

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
    path('app', views.insert_application, name='insert_application'),
    # ex: /libredb/api
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
