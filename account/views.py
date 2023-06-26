from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages as m
from .models import *
from django.http import HttpResponse
from git import Repo # 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def signup_signin(request):
    return render(request,"signup_signin.html")

def signup(request):
    if request.POST:
        f=SignupForm(request.POST)
        f.save()
        m.success(request,"Account created successfully!")
        return redirect("account:signup_signin")
    else:
        return render(request,"signup_signin.html")

def signin(request):
    if request.POST:
        uname = request.POST.get("username")
        uemail = request.POST.get("email")
        upass = request.POST.get("password")
        user = authenticate(request,username=uname,email=uemail,password=upass)

        if user is not None:
            request.session["uid"]=user.id
            login(request,user)
            return redirect("/")
        else:
            m.error(request,"Incorrect credentials.")
            return render(request,"signup_signin.html")
    else:
        return render(request,"signup_signin.html")


def signout(request):
    logout(request)
    return redirect("/account/signup-signin")

@login_required(login_url="account:signup_signin")
def booknow(request,id):

    BK_Name = request.POST.get("BK_Name")
    BK_Phone = request.POST.get("BK_Phone")
    # BK_Email = request.POST.get("BK_Email")
    BK_Email = request.user.email
    BK_travel_date = request.POST.get("BK_travel_date")
    BK_No_of_travelers = request.POST.get("BK_No_of_travelers")
    BK_uid = request.user.id
    booking = Bookings(BK_Name=BK_Name,BK_Phone=BK_Phone,BK_Email=BK_Email,BK_travel_date=BK_travel_date,BK_No_of_travelers=BK_No_of_travelers,BK_uid_id=BK_uid,BK_trip_id_id=id)
    booking.save()
    return redirect("/")

@login_required(login_url="account:signup_signin")
def mybookings(request):
    uid = request.user.id
    data = Bookings.objects.filter(BK_uid=uid)
    context = {'bookings':data}
    return render(request,"mybookings.html",context)

@login_required(login_url="account:signup_signin")
def cancel(request,id):
    cancellation = Bookings.objects.get(id=id)
    cancellation.BK_Cancel = True
    cancellation.save()
    return redirect("account:mybookings")

@login_required(login_url="account:signup_signin")
def editprofile(request):
    uid = request.user.id
    user_details = User.objects.get(id=uid)
    if request.POST:
        fn = request.POST.get("first_name")
        ln = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        profile = User.objects.get(id=uid)
        profile.first_name = fn
        profile.last_name = ln
        profile.username = username
        profile.email = email
        profile.save()
        return redirect("/")
    else:
        f=SignupForm(instance=user_details)
        context = {'form':f,'ud':user_details}
        return render(request,"editprofile.html",context)


@login_required(login_url="account:signup_signin")
def addtrip(request):
    if request.method == "POST":
        f=TripsForm(request.POST,request.FILES)
        f.save()
        return redirect("/")
    else:
        f=TripsForm
        context = {'form':f,'title':"Add Trip"}
        return render(request,'addtrip.html',context)

@login_required(login_url="account:signup_signin")
def addtripimg(request):
    if request.method == "POST":
        f=TripsImagesForm(request.POST,request.FILES)
        f.save()
        return redirect("/")
    else:
        f=TripsImagesForm
        context = {'form':f,'title':"Add Trip Images"}
        return render(request,'addtripimg.html',context)

@login_required(login_url="account:signup_signin")
def triplist(request):
    data = trips.objects.all()
    context = {'tl':data}
    return render(request,"triplist.html",context)

@login_required(login_url="account:signup_signin")
def tripdel(request,id):
    data = trips.objects.get(id=id)
    data.delete()
    return redirect("/")

@login_required(login_url="account:signup_signin")
def tripup(request,id):
    data = trips.objects.get(id=id)
    if request.method == "POST":
        f=TripsForm(request.POST,instance=data)
        f.save()
        return redirect("/")
    else:
        f=TripsForm(instance=data)
        context = {'form':f,'title':"Add Trip Images"}
        return render(request,'addtrip.html',context)
    
@csrf_exempt
def webhook(request):
    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')
    if event == 'POST':
        repo = Repo('https://github.com/Chetan1030/Tripbuddy.git')
        git = repo.git
        git.checkout('master')
        git.pull()
        return HttpResponse('pulled_success')
    return HttpResponse(status=204)

# checking