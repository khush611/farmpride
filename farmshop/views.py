from django.shortcuts import render,redirect
from django.http import HttpResponse
#from farmshop.models import Post
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import *
def home(request):
    context={

    }
    return render(request,"farmshop/homepage.html",context)
def signin(request):
    if request.method=="POST":
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        print(username,password)
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            print("I am in")
            login(request,user)
            return redirect("/dashboard/")
        else:
            return HttpResponse("user doesn't exist")
    return render(request,"farmshop/login.html")
def signup(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname',None)
        email=request.POST.get('email',None)
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        print(password)
        user_exists=User.objects.filter(username=username).exists()
        if not user_exists:
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=fullname.split()[0],
                last_name=" ".join(fullname.split()[1:])
            )
            login(request,user)
            return redirect("/dashboard/")
        else:
            return HttpResponse("User already exists.Try new username.")
    return render(request,"farmshop/signup.html")
def dashboard(request):
        context={

        }
        return render(request,"farmshop/dashboard.html",context)
def seeds(request):
    context={

    }
    return render(request,"farmshop/seeds.html",context)
def tools(request,tool_id):
        context={

        }
        return render(request,"farmshop/tools.html",context)
def manures(request,manure_id):
        context={

        }
        return render(request,"farmshop/manures.html",context)
def machines(request,machine_id):
        context={

        }
        return render(request,"farmshop/machines.html",context)
