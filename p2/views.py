from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Helloo there")
def home(request):
    return HttpResponse("<h1>lessss gooooo</h1>")
def demo1(request):
    return render(request,"sample.html")