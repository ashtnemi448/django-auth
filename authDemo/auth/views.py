from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from .models import blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.view.generic import CreateView
from django.views import TemplateView,View

# Create your views here.
@permission_required('auth.view_blog',login_url='/auth/nopermission/')
@login_required(login_url='/auth/login/')
def index(requests):
    allblg = blog.objects.all()
    blogall = {
        'blogall' : allblg
    }
    print(allblg)
    return render(requests, 'index.html',blogall)

def dash(requests):
    if requests.user.is_authenticated: 
        return HttpResponse("Invalid User")
    return HttpResponse(requests.user.username)

def login_user(request):
    if request.method == 'POST':
        nm=request.POST['user']
        p=request.POST['pass']
        user = authenticate(username=nm,password=p)
        if user is None :
             return HttpResponse("<h1> invalid </h1>")
        else:
            login(request,user)
            return redirect("/auth")
        #  return HttpResponse("<h1>"+ user.username + "</h1>"+"<h1>"+ user.password + "</h1>")
    else :
        return render(request, 'login.html')

        
def register_user(request):
    if request.method == 'POST':
        nm=request.POST['user']
        p=request.POST['pass']
        e = request.POST['e']
        created = User.objects.create_user(username=nm ,password = p, email=e)
        user = authenticate(username=nm,password=p)

        type = request.POST['type']

        if type == 'admin':
            group = Group.objects.get(name='allpermissions')
            user.groups.add(group)
        if type == 'nothing':
            group = Group.objects.get(name='nothing')
            user.groups.add(group)
        if type == 'seeonly':
            group = Group.objects.get(name='seeonly')
            user.groups.add(group)

        if user is None : 
            return HttpResponse("<h1> invalid </h1>")
        else:
            login(request,user)
            return redirect("/auth")
    else :
        return render(request, 'register.html')

def nm(request):
     return HttpResponse("<h1>"+ request.user.username + "</h1>"+"<h1>"+ request.user.password + "</h1>")

def logout_user(request):
    logout(request)
    return HttpResponse("<h1> Logged out - "+ request.user.username + "</h1>")

def nopermission(r):
    return render(r,"nopermission.html")

@permission_required('auth.add_blog',login_url='/auth/login/')
def blogwriter(request):
    if request.method == 'POST':
        body = request.POST['b']
        blg = blog()
        blg.body = body
        blg.save()
        if not request.user.is_staff : 
            return HttpResponse("<h1> invalid </h1>")
        else:
            return redirect("/auth")
    else :
        return render(request, 'blog.html')


def bloger(request):
    return render(request, 'blog.html')

class registerclass(TemplateView)
    template_name = '/auth/register/'
    def get(self, request, *args, **kwargs):
        return render('Hello, World!')
