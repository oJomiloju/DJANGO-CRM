from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, AddHomeworkForm
from .models import Record, Homework

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
          homeworks = Homework.objects.filter(record= class_record)
          return render(request,'record.html',{'class_record': class_record, 'homeworks': homeworks})
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

def delete_homework(request,record_id,homework_id):
     record = Record.objects.get(id=record_id)
     if request.user.is_authenticated:
          record = Record.objects.get(id=record_id)
          homework = Homework.objects.get(id=homework_id,record=record)
          if request.user.is_authenticated:
               homework.delete()
               messages.success(request, "Homework has been deleted successfully.")
          else:
               messages.error(request, "You must be logged in to delete homework.")
    
     return redirect('record', pk=record_id)



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

def update_homework(request, record_id, homework_id):
    record = Record.objects.get(id=record_id)
    homework = Homework.objects.get(id=homework_id,record=record)
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddHomeworkForm(request.POST, instance=homework)
            if form.is_valid():
                form.save()
                messages.success(request, "Homework has been updated successfully.")
                return redirect('record', pk=record_id)
            else:
                messages.error(request, "There was an error updating the homework. Please check the form for errors.")
        else:
            form = AddHomeworkForm(instance=homework)
    else:
        messages.error(request, "You must be logged in to update homework.")
        return redirect('home')
    
    return render(request, 'update_homework.html', {'form': form, 'record': record, 'homework': homework})



def add_homework(request,record_id):
     record = Record.objects.get(id=record_id)
     if request.method == 'POST':
          form = AddHomeworkForm(request.POST)
          if form.is_valid():
               homework = form.save(commit=False)
               homework.record = record
               homework.save()
               messages.success(request,'Homework has been added to class')
               return redirect('record',pk=record_id)
          else:
               messages.success(request,"Must be Logged in to add Homework")
     else:
          form = AddHomeworkForm()
     
     return render(request,'add_homework.html',{
          'form': form,
          'class_record': record
     })



