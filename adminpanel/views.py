from django.shortcuts import render,redirect
from adminpanel.models import regdata,coursedata,roledata,referencedata
from django.core.paginator import Paginator
from django.core.mail import send_mail
import random
# Create your views here.
def indexdata(request):
    return render(request,'index.html')


def registerdata(request):
    name=''
    email=''
    password=''
    repass=''
    err=''
    er=''
    if request.method=="POST":

        name=request.POST['name']
        print(name)
        email=request.POST['email']
        password=request.POST['pwd']
        repass=request.POST['pwd1']

        matchdata=regdata.objects.filter(Email=email)
       
       
        if matchdata.count()==0:
            
            if password==repass:
                r_data=regdata(
                    Name=name,
                    Email=email,
                    Password=password,
                    C_password=repass

                )
                r_data.save()
                return redirect('/login/')
            else:
                print("password not match!..")
        else:
           print("this email id is already exiest!..")


    return render(request,'register.html',{'err':err,'er':er})


def logindata(request):
    
    name=''
    err=''
    if request.method=="POST":
       
        email=request.POST['email']
        pwd=request.POST['pwd']
        match=regdata.objects.filter(Email=email,Password=pwd)
        if match.count()>0:
            r=regdata.objects.get(Email=email)
            name=r.Name
            request.session['name']=name
            return redirect('/index3/')
        else:
            err="please enter correct detail"

    return render(request,'login.html',{'err':err})

def index3(request):
    
    e=request.session['name']
    return render(request,'index3.html',{'e':e})

def fpassdata(request):
    if request.method=="POST":
        email=request.POST['email']
        match=regdata.objects.filter(Email=email)
        if match.count()>0:
            request.session['email']=email
            random_number=random.randrange(100000, 999999)
            request.session['random_number']=random_number
            
    
            
            send_mail(
            'That’s your subject',
            f' your random number: {random_number}',
            'riddhithummar1127@gmail.com',
            [email],
            fail_silently=False,
             )
            
            return redirect('/otp/')
        else:
            print("this email id is not exiest!!!")
    return render(request,'forgot-password.html')

# def otp(request):
  #  r=random_number
    # random_number=random.randrange(100000, 999999)
    # request.session['random_number']=random_number
    
    # emil=request.session['email']
    # #print(emil)
    # send_mail(
    #     'That’s your subject',
    #     f' your random number: {random_number}',
    #     'riddhithummar1127@gmail.com',
    #     [emil],
    #     fail_silently=False,
    # )
    #return redirect('/otp/')
    #return render(request,'otp.html')
def cotp(request):
    R=request.session['random_number']
    print(R)
    error=''
    if request.method=="POST":
        otpp=request.POST['otp'] 
         #request.session['random_number']=str(random_number)
        print(otpp)

        if str(R)==otpp:
             return redirect('/forgot-password1/')
        else:
             error='please enter correct otp!!'
        #return redirect('/forgot-password1/')
       
    return render(request,'otp.html',{'error':error})
        

def fpassdata1(request):
    email=request.session['email']
    pwd=''
    pwd1=''
    if request.method=='POST':
        pwd=request.POST['pwd']
        pwd1=request.POST['pwd1']

        if pwd==pwd1:
            data=regdata.objects.get(Email=email)
           
            data.Password=pwd
            data.C_password=pwd1
            
            data.save()

    return render(request,'forgot-password1.html')

def adddata(request):
    e=request.session['name']
    name=''
    email=''
    password=''
    repass=''
    err=''
    er=''
    if request.method=="POST":

        name=request.POST['name']
        print(name)
        email=request.POST['email']
        password=request.POST['pwd']
        repass=request.POST['pwd1']

        matchdata=regdata.objects.filter(Email=email)
       
        if matchdata.count()==0:
            
            if password==repass:
                r_data=regdata(
                Name=name,
                Email=email,
                Password=password,
                C_password=repass

                )
                r_data.save()
            else:
                print("password not match!..")
        else:
           print("this email id is already exiest!..")
    return render(request,'adddata.html',{'e':e})

def viewdata(request):
    e=request.session['name']
    data=regdata.objects.all()
    if request.method=="POST":
        search=request.POST['search']
        data=regdata.objects.filter(Name=search)
    paginator = Paginator(data, 7)
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    return render(request,'viewdata.html',{'page_obj':page_obj,'e':e})

def addcourse(request):
    e=request.session['name']
    course=''
    if request.method=="POST":
        course=request.POST['course']

        c=coursedata(
            Course=course
        )
        c.save()
    return render(request,'addcourse.html',{'e':e})
    
def viewcourse(request):
    e=request.session['name']
    viewdata=coursedata.objects.all()
    if request.method=="POST":
        search=request.POST['search']
        viewdata=coursedata.objects.filter(Course=search)
    paginator = Paginator(viewdata, 7)
    page_number = request.GET.get('page')
    
    page_obje = paginator.get_page(page_number)

    return render(request,'viewcourse.html',{'page_obje':page_obje,'e':e})

def deletedata(request,id):
    regdata.objects.filter(id=id).delete()
    return redirect('/viewdata/')

def editdata(request,id):
    e=request.session['name']
    edit=regdata.objects.get(id=id)

    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']

        edit.Name=name
        edit.Email=email
        edit.save()
    return render(request,'editdata.html',{'edit':edit,'e':e})

def deletecourse(request,id):

    coursedata.objects.filter(id=id).delete()
    return redirect('/viewcourse/')
def editcourse(request,id):

    e=request.session['name']
    e_course=coursedata.objects.get(id=id)
    if request.method=="POST":
        course=request.POST['course']
        e_course.Course=course

        e_course.save()
    return render(request,'editcourse.html',{'e_course':e_course,'e':e})

def Roledata(request):
    e=request.session['name']
    role=''
    if request.method=="POST":
        role=request.POST['role']

        roledt=roledata(
            Role=role
        )
        roledt.save()

    return render(request,'addrole.html',{'e':e})

def viewrole(request):
    e=request.session['name']
    viewdata=roledata.objects.all()
    if request.method=="POST":
        role=request.POST['role']
        viewdata=roledata.objects.filter(Role=role)
    paginator = Paginator(viewdata, 7)
    page_number = request.GET.get('page')
    
    page_obje = paginator.get_page(page_number)

    return render(request,'viewrole.html',{'page_obje':page_obje,'e':e})


def deleterole(request,id):
    roledata.objects.filter(id=id).delete()
    return redirect('/viewrole/')

def editrole(request,id):
    e=request.session['name']
    e_role=roledata.objects.get(id=id)
   
    
    if request.method=="POST":
        role=request.POST['rolee']
        e_role.Role=role    
        e_role.save()

    return render(request,'editrole.html',{'e_role':e_role,'e':e})

def addreference(request):
    e=request.session['name']
    if request.method=="POST":
        reference=request.POST['reference']
        r_data=referencedata(
            Reference=reference
        )
        r_data.save()
    return render(request,'addreference.html',{'e':e})

def viewreference(request):
    e=request.session['name']
    viewref=referencedata.objects.all()
    if request.method=="POST":
        ref=request.POST['search']
        viewref=referencedata.objects.filter(Reference=ref)
    paginator = Paginator(viewref, 7)
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    return render(request,'viewreference.html',{'page_obj':page_obj,'e':e})

def deletereference(request,id):
    referencedata.objects.filter(id=id).delete()
    return redirect('/viewreference/')

def editreference(request,id):
    e=request.session['name']
    e_ref=referencedata.objects.get(id=id)
    if request.method=="POST":
        ref=request.POST['reference']
        e_ref.Reference=ref
        e_ref.save()
    return render(request,'editreference.html',{'e_ref':e_ref,'e':e})



