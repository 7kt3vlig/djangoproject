from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")


def sjukt3vlig(request):
    return HttpResponse("Hello, 7kt3vlig!")


def greet(request, name): 
        return HttpResponse(f"Hello, {name.capitalize()}!")


