# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request):
  return HttpResponse("hello world")

def detail(request, param1):
  return HttpResponse(`param1`)

def not_found(request):
  return render(request, '404.html', {}, status=404)
