from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import models
from .models import BOOKS_TBL,ORDERS_TBL


# Create your views here.

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        fname=request.POST["firstname"]
        lname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        confirm=request.POST['confirm']

        #check if username already exists
        if User.objects.filter(username=username):
            messages.error(request,"username  already exists")
            return redirect('login:login')
        #check if email alrady exists
        if User.objects.filter(email=email):
            messages.error(request,"a user with the email already exists login instead")
            return redirect('login:login')

        if password != confirm:
            messages.error(request,"passwords didn't match")

        #create a user with the credentials
        visitor=User.objects.create_user(username,email,password)
        visitor.first_name=fname
        visitor.last_name=lname
        visitor.save()

        messages.success(request, "you account was successfully created login")

        return redirect('login:login')
    return render(request,'home/register.html')

def login_user(request):
    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        #user authentication
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            fname=user.first_name

            return render(request,"home/home.html",
                          {'fname':fname ,
                           "books":BOOKS_TBL.objects.all()})
        
        else:
            messages.error(request,"incorrect username or password")
            return redirect("login:register")
    return render(request,'home/login.html')

def signout(request):
    logout(request)
    messages.success(request,"you are logged out successfully")
    return redirect('login:login')


def profile_picture(request):
    if request.method=="POST":
        profile_pic=request.POST["image"]

    
    
    
    