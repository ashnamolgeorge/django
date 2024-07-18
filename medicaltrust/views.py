from django.shortcuts import render,redirect
from adminhandle.models import*
from.models import*

# Create your views here.
def medical(request):
    return render(request,"userface.html")


def trust(request):
    data=Doctors.objects.all()
    return render(request,"detailed.html",{'data':data})

def booking(request,id):
    data=Doctors.objects.filter(id=id)
    return render(request,"booking.html",{'data':data})

def appoinment(request):
    data=Doctors.objects.all()
    return render(request,"appoinment.html",{'data':data})



def home(request):
    return render(request,"home.html")

def service(request):
    return render(request,"service.html")

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        your_message=request.POST['your_message']
        data=Contacts(name=name,email=email,phone=phone,subject=subject,your_message=your_message)
        data.save()
    return render(request,"contact.html")

def Register(request):
    if request.method=='POST':
        name=request.POST['name'] 
        email=request.POST['email']
        password=request.POST['password']
        contact=request.POST['contact']
        data=Registration(name=name,email=email,password=password,contact=contact)
        data.save()
    return render(request,"register.html")    


def list(request,id):
    data=Doctors.objects.filter(id=id)
    return render(request,"doctors.html",{'data':data})
    
def Ulogin(request):
    return render(request,"login.html")



def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Registration.objects.filter(name=username,password=password).exists():
           data = Registration.objects.filter(name=username,password=password).values('email','id','contact').first()
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['contact'] 
           request.session['email_u'] = data['email'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('medical') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('Ulogin')

def userlogout(request):
    
    del request.session['u_id']

    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('login') 

def acdata(request,id):
    if request.method=='POST':
       user_id=request.session.get('u_id') 
    #    doctor_id=request.POST['doctor_id']
       date=request.POST['date']
       time=request.POST['time']
       data=myac(user_id=Registration.objects.get(id=user_id),
                 doctor_id=Doctors.objects.get(id=id),date=date,time=time
                 )
       data.save()
    return redirect('booking',id)   


def activity(request):
    data=myac.objects.filter(status=0)
    return render(request,"activity.html",{'data':data})   


def cancel(request,id):
    data=myac.objects.filter(id=id).delete()
    return redirect('medical')











