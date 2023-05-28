from django.shortcuts import render
# Se importa HttpResponse
from django.http import HttpResponse
# Create your views here.
def index(request):
return HttpResponse("Hola desde mi primera vista ")
def index(request):
    return HttpResponse("Autor: Brenda Montaño")

