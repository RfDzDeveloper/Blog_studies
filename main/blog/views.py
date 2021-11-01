from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import django.contrib.messages as messages
from database.database_service import DatabaseService
from blog.models import Post, Comment

def home(request: HttpRequest):
    return render(request, "home.html")

@login_required(login_url='login')
def read_posts(request: HttpRequest):    
    try:
        posts: list[Post] = Post.objects.filter(id= request.user.id)
        context: dict = {'posts': posts}
        return render(request, 'read_posts.html', context)
    except Exception as ex:
        messages.error(request, ex)
        raise Http404

def login_view(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('read_posts')    
    
    if request.method == "POST":
        try:            
            username: str = request.POST['username']
            password: str = request.POST['password']
            if username != " " and password != " ":
                user = authenticate(username = username, password = password)
                
                if user != None:                        
                    login(request, user)                     
                    context: dict = {'message': 'Successful login!'}
                    messages.success(request, context['message'])
                    return redirect('read_posts')            
                else:
                    context: dict = {'message': 'Wrong login attempt.'}
                    messages.error(request, context['message'])
                    return render(request, 'login')
        except Exception as ex:            
            messages.add_message(request, messages.ERROR, ex)
            return render(request, 'login')
    else:
        return render(request, 'login')    

def logout_view(request: HttpRequest):
    logout(request)
    return render(request, 'logout.html')

def register(request: HttpRequest):
    if request.method == 'POST':
        try:
            user: User = DatabaseService().add_user(request)
            context: dict = {'message': f'Successful register user: {user.username}.\nPlease login!'}
            messages.success(request, context['message'])
            return redirect('login')
        except Exception as ex:
            messages.error(request, ex)
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

@login_required(login_url='login')
def add_post(request: HttpRequest):
    return render(request, 'add_post.html')

@login_required(login_url='login')
def view_user_post(request: HttpRequest):
    return render(request, 'view_user_posts')

@login_required(login_url='login')
def delete_post(request: HttpRequest):
    return redirect("view_user_post")
