from django.shortcuts import render
from django.http.request import HttpRequest

def home(request: HttpRequest):
    return render(request, "home.html")

def read_posts(request: HttpRequest):
    return render(request, 'read_posts.html')

def login_view(request: HttpRequest):
    return render(request, 'login.hmtl')

def logout_view(request: HttpRequest):
    return render(request, 'logout.html')

def register(request: HttpRequest):
    return render(request, 'register.html')
