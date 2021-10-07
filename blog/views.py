from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignupForm, LoginForm, PostForm
from django.contrib import messages
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html',{'posts':posts})

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user)
        return render(request, 'blog/dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')

def user_signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Registered Successfully!!!')
            fm.save()
            fm = SignupForm()
    else:
        fm = SignupForm()
    return render(request, 'blog/signup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully!!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = LoginForm()
        return render(request, 'blog/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged Out Successfully!!!')
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def update_post(request, id):
    pi = Post.objects.get(pk=id)
    if request.user.is_authenticated and pi.user==request.user:
        if request.user.is_authenticated:
            if request.method == 'POST':
                pi = Post.objects.get(pk=id)
                fm = PostForm(request.POST, instance = pi)
                if fm.is_valid():
                    fm.save()
                    messages.success(request, 'Post Updated Successfully!!!')
                    return HttpResponseRedirect('/dashboard/')
            else:
                pi = Post.objects.get(pk=id)
                fm = PostForm(instance=pi)
            return render(request, 'blog/updatepost.html',{'form':fm})
        else:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/dashboard/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PostForm(request.POST)
            if fm.is_valid():
                print(request.user.id)
                uid = request.user.id
                utitle = fm.cleaned_data['title']
                udesc = fm.cleaned_data['desc']
                tmp = Post(user=request.user,title=utitle,desc=udesc)
                tmp.save()
                messages.success(request, 'Post Created Successfully!!!')
                fm = PostForm()
                return HttpResponseRedirect('/dashboard/')
        else:
            fm = PostForm()
        return render(request, 'blog/addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request, id):
    pi = Post.objects.get(pk=id)
    if request.user.is_authenticated and pi.user==request.user:
        if request.user.is_authenticated:
            if request.method == 'POST':
                pi = Post.objects.get(pk=id)
                pi.delete()
                return HttpResponseRedirect('/dashboard/')
            else:
                return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/dashboard/')