from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def hola_mundo (request):
    return HttpResponse("Hola mundo Django")