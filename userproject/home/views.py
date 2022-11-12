
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

# Create your views here.

#   password ankit@2001

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            # now  logining user
            login(request, user)
            return redirect("/")
        else:# No backend authenticated the credentials
             return  render(request,'login.html')
    return render(request,'login.html')

   
    
def logoutUser(request):
    logout(request)
    return redirect("/login")
    # return render(request,'index.html')
    # render(request,'logout.html')