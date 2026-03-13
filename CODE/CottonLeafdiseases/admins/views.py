from django.shortcuts import render, redirect
from user.models import UserReg
# Create your views here.

def adminhome(request):
    return  render(request, 'admins/adminhome.html')
def adminlogin(request):
    if request.method =='POST':
        username=request.POST.get('loginid')
        password = request.POST.get('pswd')
        if username=='admin' and password=='admin':
            return redirect('adminhome')
        else:
            return redirect('adminlogin')
    return render(request, 'AdminLogin.html')


def  userdeatails(request):
      details = UserReg.objects.all()
      return render(request , 'admins/viewregisterusers.html' , {'details' : details })
  
def ActivateUser(request):
    if request.method =='GET':
        id=request.GET.get('uid')
        status='Activated'
        UserReg.objects.filter(id=id).update(status=status)
        details=UserReg.objects.all()
    return render(request , 'admins/viewregisterusers.html' , {'details' : details})

def Deleteuser(request):
    if request.method=='GET':
        id=request.GET.get('uid')
        UserReg.objects.get(id=id).delete()
        details = UserReg.objects.all()
    return render(request , 'admins/viewregisterusers.html' , {'details' : details})