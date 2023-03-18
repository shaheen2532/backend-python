from django.http import HttpResponse 
from django.shortcuts import render

def page1(request):
    title = 'HI THERE'
    return render(request, 'files/mproject.html', {'data': title, "mylist":[1,2,3,4]})

