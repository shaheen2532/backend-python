from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello there') 

def page1(request):
    return render(request, 'files/mproject.html', {'data': 'test-data'})

