from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(resuest):
    return HttpResponse('Hello word. you are at the polls index')