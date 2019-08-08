
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader

from rest_framework import viewsets
from .serializers import ApplicationSerializer, ArticleSerializer, PillSerializer

from .models import Application, Article, Pill

#def index(request):
#    return HttpResponse("Hello, world. You're at the db index.")

def index(request):
    latest_application_list = Application.objects.order_by('app_name')[:5]
    #template = loader.get_template('libredb/index.html')
    context = {
        'latest_application_list': latest_application_list,
    }
    return render(request, 'libredb/index.html', context)

def detail(request, app_full_name):
    application = get_object_or_404(Application, app_full_name=app_full_name)
    return render(request, 'libredb/detail.html', {
        'application' : application,
        'libre' : application.app_libre,
        'usability' : application.app_usability,
        'porting' : application.app_porting,
        'potential' : application.app_potential,
        'design' : application.app_design,
        'average' : (
            int(application.app_libre) +
            int(application.app_usability) +
            int(application.app_porting) +
            int(application.app_potential) +
            int(application.app_design))/5,
        'libre_rate' : ['●' if i < int(application.app_libre) else '○' for i in range(5)],
        'usability_rate' : ['●' if i < int(application.app_usability) else '○' for i in range(5)],
        'porting_rate' : ['●' if i < int(application.app_porting) else '○' for i in range(5)],
        'potential_rate' : ['●' if i < int(application.app_potential) else '○' for i in range(5)],
        'design_rate' : ['●' if i < int(application.app_design) else '○' for i in range(5)],
})

def results(request, app_name):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % app_name)

def vote(request, app_name):
    return HttpResponse("You're voting on question %s." % app_full_name)

@login_required
def insert_application(request):
    #query_results = Application.objects.order_by('app_name')

    return HttpResponse("you are viewing the db")


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('app_full_name')
    print(queryset)
    serializer_class = ApplicationSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    variable_column = 'art_state'
    search_type = 'contains'
    filter = variable_column + '__' + search_type
    search_string = 'PU'
    queryset = Article.objects.filter(**{filter: search_string})
    serializer_class = ArticleSerializer

class PillViewSet(viewsets.ModelViewSet):
    variable_column = 'pil_state'
    search_type = 'contains'
    filter = variable_column + '__' + search_type
    search_string = 'PU'
    queryset = Pill.objects.filter(**{filter: search_string})
    serializer_class = PillSerializer
