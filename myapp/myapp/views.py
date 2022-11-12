

from datetime import datetime
from django.shortcuts import render


def home(request):
    isActive = False
    # taking client data here...
    if request.method=="POST":
        nameinput=request.POST['nameinput']
        checkinput = request.POST.get("checkinput")

        #if checkbox ya radio hai tou es kro then exception nahi lagana padega..if value hogi tou value aayega or else none aayega
        #  nameinputradio_or_checkbox=request.POST.get('nameinput')
        if checkinput is None:isActive=False
        else: isActive=True
        print(nameinput)

    # date = datetime.datetime.now()
    date = datetime.now()
    # isActive = False
  
    name='Steve Jobs'
    list_of_programs = ['WAP to check even or odd..',
    'wap to check prime number',
    'wap to print pascals triangle'
    ]
    student= { 
   'student_name' : 'yoyo',
    'student_col': 'ZYX',
    'student_city':'NY'
     }

    datasend = {
    'date':date,
    'isActive':isActive,
    'name':name,
    'list_of_programs':list_of_programs,    
    'student_data':student,
   
    }

    return render(request,"home.html",datasend)



def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")