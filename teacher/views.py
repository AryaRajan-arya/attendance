from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return HttpResponse('home')

def student (request):
    return HttpResponse('student')

def attend (request):
    return HttpResponse('attend')
# Create your views here.
