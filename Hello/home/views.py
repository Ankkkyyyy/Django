from datetime import datetime
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

from home.models import Contact

from django.contrib import messages
# Create your views here.


def index(request):
    context = {
        'variable':"Ankit"
    }
    # return HttpResponse("This is Response...")
    return render(request,'index.html',context)


def about(request):
    # return HttpResponse("About....")  
    return render(request,"about.html")

def services(request):
     return render(request,'services.html')

def contact(request):
    # return HttpResponse("....contacts...") 
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent.')

    return render(request,'contact.html')