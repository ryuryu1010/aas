from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("ようこそ")
# Create your views here.
