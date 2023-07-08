from django.shortcuts import render
from django.http import HttpResponse

def log(request):
    return HttpResponse("So you want to log stuff?")