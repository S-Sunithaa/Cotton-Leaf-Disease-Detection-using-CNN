"""CottonLeafdiseases URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from CottonLeafdiseases import views as a
from user import views as b
from admins import views as c
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', a.index , name='index'),
    # path('userlogin/', a.userlogin , name='userlogin' ),
    #path('adminlogin/' , a.adminlogin , name='adminlogin'),
    
    #user urls
    path('userhome' , b.userhome , name='userhome' ),
    path('userregister/' , b.UserRegister , name='userregister'),
    path('userlogin/', b.userlogin , name='userlogin'),
    
    #admins urls
    path('adminhome/', c.adminhome , name='adminhome'),
    path('adminlogin/', c.adminlogin , name='adminlogin'),
    path('viewuser/' , c.userdeatails , name='viewuser'),
    path('activateuser/' , c.ActivateUser , name='activateuser'), 
    path('deleteuser/', c.Deleteuser , name='deleteuser'), 
    
    #Predication
    path('pedication/', b.Predication , name='predication')
] +static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
