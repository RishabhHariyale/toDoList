# Create your views here.

from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from app.forms import TODOForm
from .models import ToDo
from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.success(request,"Username already Exits")
                return redirect ("login/#")

            elif User.objects.filter(email = email).exists():
                messages.success(request , "Email Already Taken!!")
                return redirect ("login/#")

            else:
                user = User.objects.create_user(username = username , email = email , password = password2)
                user.save()
                return redirect("/login")

        else:
            messages.warning(request , "Password is not matching!!")
            return redirect("login")

    else:
        return render(request , "login.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username , password = password)
        if user is not None:
            auth_login(request , user)
            return redirect('home')
        # else:
        #     messages.error(request , "Invalid Username or Password")
        #     return redirect("login")
    else:
        return render (request , "login.html")

def logout(request):
    auth_logout(request)
    return redirect ("/")

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = ToDo.objects.filter(user = user ).order_by('priority')
        return render(request, 'index.html' , context= {'form' : form , 'todos' : todos})
    

def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit = False)
            todo.user = user
            todo.save()
            return redirect("home")
        else:
            return render(request, 'index.html' , context= {'form' : form})


def delete_todo(request ,id):
    ToDo.objects.get(pk = id).delete()
    return redirect('home')



def change_status(request ,id , status ):
    todo = ToDo.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')