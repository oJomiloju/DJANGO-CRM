from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
        records = Record.objects.all()
        return render(request,'home.html',{
             'records': records
        })

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
    if request.method == 'POST':
         form = SignUpForm(request.POST)
         if form.is_valid():
              form.save()
              # AUTHENTICATE AND LOGIN
              username = form.cleaned_data['username']
              password = form.cleaned_data['password1']
              user = authenticate(username=username,password=password)
              login(request,user)
              messages.success(request,"successfully registered")
              return redirect('home')
    else:
         form = SignUpForm()  
         return render(request,'register.html',{
              'form': form
         })
    
    return render(request,'register.html',{
              'form': form
         })
def about(request):
    return render(request,'about.html')

def class_record(request,pk):
     if request.user.is_authenticated:
          # Look up RECORDS 
          class_record = Record.objects.get(id=pk)
          return render(request,'record.html',{'class_record': class_record})
     else:
          messages.success(request,"You Must be Logged In To View Record")
          return redirect('home')

def delete_record(request,pk):
     if request.user.is_authenticated:
          class_record = Record.objects.get(id=pk)
          class_record.delete()
          messages.success(request,"Class has been deleted...")
          return redirect('home')
     else:
          messages.success(request,"Must be logged in to delete class...")
          return redirect('home')

def add_record(request):
     form = AddRecordForm(request.POST or None)
     if request.user.is_authenticated:
          if request.method == "POST":
               if form.is_valid():
                    add_record = form.save()
                    messages.success(request,"Class was successfully added...")
                    return redirect('home')
          return render(request,'add_record.html',{
               'form': form
          })
     else:
          messages.success(request,"Must be Logged In...")
          return redirect('home')


def update_record(request,pk):
     if request.user.is_authenticated:
          current_record = Record.objects.get(id=pk)
          form = AddRecordForm(request.POST or None, instance=current_record)
          if form.is_valid():
               form.save()
               messages.success(request,"Record Has Been Updated")
               return redirect('home')
          return render(request, 'update_record.html',{'form': form})
     else:
          messages.success(request,"Must be Logged In")
          return redirect('home')
          

