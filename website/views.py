from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
        return render(request,'home.html',{})

def login_user(request):
    # CHECK TO SEE IF LOGGING IN 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # AUTHENTICATE USER 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged in!")
            return redirect('home')
        else:
            messages.success(request,"ERROR LOGGING IN. PLEASE TRY AGAIN...")
            return redirect('login')
    return render(request,'login.html')

def logout_user(request):
    # JUST CALL LOGOUT FUNCTION 
    logout(request)
    messages.success(request,"You Have been Logged Out...")
    return redirect('home')

def register_user(request):
     return render(request,'register.html',{})

def about(request):
    return render(request,'about.html')