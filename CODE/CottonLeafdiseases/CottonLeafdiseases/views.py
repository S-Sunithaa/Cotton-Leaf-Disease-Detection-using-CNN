from django.shortcuts import render , redirect

def base(request):
    return render(request , "base.html")

def index(request):
    return render(request ,'index.html')

def adminlogin(request):
    return render(request , 'AdminLogin.html')


def userlogin(request):
    return render(request , 'UserLogin.html')

