from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello word. you are at the polls index')


def detail(request, question_id):
    return HttpResponse("You're looking at question %s,%s." % (question_id, request.GET.get('id')))
