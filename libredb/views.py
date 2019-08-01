from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the db index.")


def detail(request, app_name):
    return HttpResponse("Nome applicazione %s." % app_name)

def results(request, app_name):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % app_name)

def vote(request, app_name):
    return HttpResponse("You're voting on question %s." % app_name)
