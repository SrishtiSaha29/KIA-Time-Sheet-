from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import *
from django.http import JsonResponse
from .forms import CheckInForm
from .models import TimeSheet
from django.http import HttpResponseRedirect
import datetime

from django.http import HttpResponse
from .tasks import *
from django.shortcuts import render
import time
import schedule



from django.http import HttpResponse

import json

# Create your views here.


def index(request):
    
    return render(request,'index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form=CreateEmpForm()
        if request.method=='POST':
            form=CreateEmpForm(request.POST)
            if form.is_valid():
                user=form.save()
                username=form.cleaned_data.get('username')
                group=Group.objects.get(name='employee')
                user.groups.add(group)
                Employees.objects.create(user=user,empname=user.username,email=user.email)
                messages.success(request,'User Successfully created for '+username)
                return redirect('register')
    context={'form':form}        
    return render(request,'register.html',context)


def Loginpage(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/') 
        else:
            messages.info(request,'empname or password error')
            print("employee_name or password error ")
            return redirect('Loginpage')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('/')


# def check_in(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST)
        if form.is_valid():
            empname = form.cleaned_data['empname']
            place = form.cleaned_data['place']
            ip_address = request.META.get('REMOTE_ADDR')  # Get IP address

            # Create a new entry in the TimeSheet model
            time_sheet = TimeSheet.objects.create(
                empname=empname,
                place=place,
                ip_address=ip_address,
                day=datetime.date.today(),
                time=datetime.datetime.now().time()
            )
            time_sheet.save()

            # Redirect to a success page or render a success message
            return HttpResponseRedirect('//127.0.0.1:8000/')  # Replace '/success/' with your success URL

    else:
        form = CheckInForm()

    return render(request, 'index.html', {'form': form})

def check_in(request):
    # Check if the user has already checked in
     # Check if the user has already checked in
    if Employees.objects.filter(user=request.user).exists():
        return JsonResponse({'success': False, 'message': 'Already checked in.'})

    else:
      Employees.objects.create(user=request.user)

    return JsonResponse({'success': True, 'message': 'Check-in successful'})
    # user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    # if user_ip:
    #     ip = user_ip.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    
    # return HttpResponse("Welcome User!<br>You are visiting from: {}".format(ip))
    
  
        

    # # Process the check-in
    # Employees.objects.create(user=request.user)

    # return JsonResponse({'success': True, 'message': 'Check-in successful'})


# def job():
#     print("Job is running...")

# # Schedule the job to run every day at 2:30 PM
# schedule.every().day.at("12:35").do(job)

# # You can add more scheduled jobs here

# while True:
#     schedule.run_pending()
#     time.sleep(1)


# def retrieve_user_ip(ip_address):

#         # Get the client's IP address from the request object
#     client_ip = request.META.get('REMOTE_ADDR')

#     # # Do something with the client's IP address, for example, print it
#     print(f"Client IP Address: {client_ip}")

#     # #Return a simple HTTP response
#     return HttpResponse("Check your server logs for the client's IP address.<br>Welcome User!<br>You are visiting from: {}".format(client_ip))



