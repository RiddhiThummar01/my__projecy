"""
URL configuration for admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from adminpanel.views import indexdata,registerdata,logindata,index3,fpassdata,cotp,adddata,viewdata,fpassdata1,addcourse,viewcourse,deletedata,editdata,deletecourse,editcourse,Roledata,viewrole,deleterole,editrole,addreference,viewreference,deletereference,editreference

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',indexdata),
   
    path('register/',registerdata),
    path('login/',logindata),
    path('index3/',index3),
    path('forgot-password/',fpassdata),
    path('adddata/',adddata),
    path('viewdata/',viewdata),
    path('forgot-password1/',fpassdata1),
   # path('otp/',otp),
    path('otp/',cotp),


    path('addcourse/',addcourse),
    path('viewcourse/',viewcourse),
    path('delete/<int:id>',deletedata),
    path('edit/<int:id>',editdata),
    path('deletee/<int:id>',deletecourse),
    path('editdata/<int:id>',editcourse),
    path('addrole/',Roledata),
    path('viewrole/',viewrole),
    path('deleterole/<int:id>',deleterole),
    path('editrole/<int:id>',editrole),
    path('addreference/',addreference),
    path('viewreference/',viewreference),
    path('deletereference/<int:id>',deletereference),
    path('editreference/<int:id>',editreference)

]

