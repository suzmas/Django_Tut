from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "This message"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse("This is the about page. The index page is located at <a href='/rango/'>Index</a>")
