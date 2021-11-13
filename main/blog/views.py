from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import django.contrib.messages as messages
from blog.database.database_service import DatabaseService
from blog.models import Post, Comment


def home(request: HttpRequest):
    return render(request, "home.html")

@login_required(login_url='login')
def my_home(request: HttpRequest):   
    try: 
        context: dict = {'post_list': DatabaseService().get_new_posts()}
        return render(request, "my_home.html", context)
    except Exception as ex:
        messages.error(request, ex)
        return redirect('home')

@login_required(login_url='login')
def view_all_posts(request: HttpRequest):
    try:
        context: dict = {'post_list': DatabaseService().get_all_posts(20)}
        return render(request, 'view_all_posts.html', context)
    except Exception as ex:
        messages.error(request, ex)
        return redirect('my_world')
    
@login_required(login_url='login')
def read_post(request: HttpRequest, post_id: int):    
    try:
        context: dict = {'post': Post.objects.filter(id=post_id),
                         'comments': Comment.objects.filter(
                             post__id=request.POST['post_id']).order_by('publish_date')}        
        return render(request, 'read_posts.html', context)
    except Exception as ex:
        messages.error(request, ex)
        raise Http404

def login_view(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('my_home')    
    
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
    if request.method == 'POST':
        try:
            post: Post = DatabaseService().add_post(request)
            context: dict = {'message': 'Successful added post',
                             'post': post}
            return render(request, 'add_post.html', context)
        except Exception as ex:
            messages.error(request, ex)            
            return render(request, 'add_post.html')
    else:
        return render(request, 'add_post.html')    

@login_required(login_url='login')
def edit_post(request: HttpRequest):
    if request.method == 'POST':
        try:            
            context: dict = {'message': 'Successful edit post',
                             'post': DatabaseService().edit_post(request)}
            messages.success(request, context['message'])
            return redirect('view_user_post')
        except Exception as ex:
            messages.error(request, ex)
            return redirect('my_world')
    else:
        return render(request, 'edit_post.html')
    
@login_required(login_url='login')
def view_user_post(request: HttpRequest):
    try:
        post_list: list[Post] = Post.objects.filter(user__id=request.user.id)
        context: dict = {'post_list': post_list}
        return render(request, 'view_user_posts', context)
    except Exception as ex:
        messages.error(request, ex)
        return redirect('my_home')        

@login_required(login_url='login')
def delete_post(request: HttpRequest):
    try:
        DatabaseService().delete_post(request)        
        context: dict = {"message": "Successful added post."}
        messages.success(request, context['message'])        
    except Exception as ex:
        messages.error(request, ex)
    return redirect('view_user_post')

@login_required(login_url='login')
def add_comment(request: HttpRequest):
    try:
        DatabaseService().add_comment(request)               
    except Exception as ex:
        messages.error(request, ex)
    return redirect('read_post', post_id=request.POST['post_id'])

@login_required(login_url='login')
def edit_comment(request: HttpRequest):
    try:
        DatabaseService().edit_comment(request)
    except Exception as ex:
        messages.error(request, ex)
    return redirect('read_post', post_id=request.POST['post_id'])        
