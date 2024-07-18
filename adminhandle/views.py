from django.shortcuts import render,redirect
from.models import*
from medicaltrust.models import*

# Create your views here.
def details(request):
    table=Doctors.objects.all().count()
    usertable=Registration.objects.all().count()
    Ucontact=Contacts.objects.all().count()
    actable=myac.objects.filter(status=0).count()
    aptable=myac.objects.filter().count()
    return render(request,"adminindex.html",{'table':table,'usertable':usertable,'Ucontact':Ucontact,'actable':actable,'aptable':aptable})

def form(request):
    if request.method=="POST":
       category=request.POST['category'] 
       doctors_name=request.POST['doctors_name']
       doctor_image=request.FILES['doctor_image']
       data=Doctors(category=category,doctors_name=doctors_name,doctor_image=doctor_image)
       data.save()
    return render(request,"index.html")

def table(request):
    data=Doctors.objects.all()
    return render(request,"table.html",{'data':data})

def usertable(request):
    data=Registration.objects.all()
    return render(request,"usertable.html",{'data':data})

def Ucontact(request):
    data=Contacts.objects.all()
    return render(request,"contacttable.html",{'data':data})

def add(request):
    if request.method=='POST':
        category=request.POST['category']
        doctors_name=request.POST['doctors_name']
        doctors_image=request.POST['doctors_image']
        experiance=request.POST['experiance']
        contact=request.POST['contact']
        data=Doctors(category=category,doctors_name=doctors_name,
                     doctors_image=doctors_image,experiance=experiance,
                     contact=contact)
        data.save()
    return render(request,"index.html") 

def actable(request):
    data=myac.objects.filter(status=0)
    return render(request,"actable.html",{'data':data})   


def remove(request,id):
    data=myac.objects.filter(id=id).update(status=2)
    return redirect('aptable')


def approve(request,id):
    data=myac.objects.filter(id=id).update(status=1)
    return redirect('aptable')


def aptable(request):
    data=myac.objects.filter(status=1)
    return render(request,"approved.html",{'data':data})


