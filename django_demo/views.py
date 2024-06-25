# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World! I'm home")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("I'm the about page")
    return render(request, 'about.html')