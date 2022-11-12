from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Emp,Testimonial
from .form import FeedbackForm

# Create your views here.

def emp(request):
    return HttpResponse("Yo Yo Welcome !")

def emp_home(request):
    emps = Emp.objects.all()

    # return HttpResponse("Yo Yo Employee Page ! ")
    return render(request,"emp/home.html",{'emps':emps})


def add_emp(request):
    if request.method == "POST":
        #  Data fetch
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address") 
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")    
        # Creating Model object & setting the data
        e = Emp()
        e.name = emp_name
        e.emp_id=emp_id
        e.phone = emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        # Saving the object 
        #prepare mssge ..
 
        print("data is comming....")
        return redirect("/employee/home")
    # return HttpResponse("Yo Yo Employee Page ! ")
    return render(request,"emp/add_emp.html")

def delete_emp(request,emp_id):
    emp =Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/employee/home")

def update_emp(request,emp_id):
    emp =Emp.objects.get(pk=emp_id)
    # emp.delete()
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })
    # return redirect("/employee/home")

def do_update_emp(request,emp_id):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address") 
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")    

        e = Emp.objects.get(pk=emp_id)
        e.name = emp_name
        e.emp_id=emp_id_temp
        e.phone = emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()


    return redirect("/employee/home/")

def testimonials(request):
    testi = Testimonial.objects.all()

    return render(request,"emp/testimonial.html",{'testi':testi})

def feedback(request):
    if request.method=="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            
            print("data saved !")
        else:
            return render(request,"emp/feedback.html",{"form":forms})


    else:
        forms = FeedbackForm()
    return render(request,"emp/feedback.html",{"form":forms})



 #  Django Admin Credentials .....
# username - ankit,ankitxtowod@gmail.com
# password - ankit 