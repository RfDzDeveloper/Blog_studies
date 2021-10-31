from django.shortcuts import render
from django.http.request import HttpRequest

def home(request: HttpRequest):
    return render(request, "home.html")

def read_posts(request: HttpRequest):
    return render(request, 'read_posts.html')
