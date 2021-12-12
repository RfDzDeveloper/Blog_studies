from django.http import HttpRequest
from django.shortcuts import redirect, render

def home(requset: HttpRequest):
    return render(requset, 'welcome_site.html')