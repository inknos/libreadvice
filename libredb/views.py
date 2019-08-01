from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Application

#def index(request):
#    return HttpResponse("Hello, world. You're at the db index.")

def index(request):
    latest_application_list = Application.objects.order_by('-app_name')[:5]
    template = loader.get_template('libredb/index.html')
    context = {
        'latest_application_list': latest_application_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, app_name):
    return HttpResponse("Nome applicazione %s." % app_name)

def results(request, app_name):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % app_name)

def vote(request, app_name):
    return HttpResponse("You're voting on question %s." % app_name)

