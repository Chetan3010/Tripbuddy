from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages as m
from .models import *
import smtplib
import ssl
from email.message import EmailMessage
import math, random
from django.shortcuts import get_object_or_404
from django.http import Http404

email_sender = 'tripbuddy.in@gmail.com'
email_password = 'pxrwozlyauqvzlxj'

def signup_signin(request):
    return render(request,"signup_signin.html")

def signup(request):
    if request.POST:
        f=SignupForm(request.POST)
        if f.is_valid():
            f.save()
            m.success(request,"Account created successfully!")
        else:
            m.error(request,"Given credentials didn't validate!")
            context = {'signup':True}
            return render(request,"signup_signin.html",context)
        return redirect("account:signup_signin")
    else:
        return render(request,"signup_signin.html")

def signin(request):
    if request.POST:
        uname = request.POST.get("username")
        uname = uname.lower()
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
        try:
            profile.save()
        except Exception as e:
            m.error(request,e)
            return redirect("account:edit-profile")
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
    
def generateOTP(request,email):
    OTP = 0
    for i in range(4):
        dig = math.floor(random.random() * 10)
        OTP = (OTP * 10) + dig

    email_receiver = email
    subject = 'Tripbuddy password assitance'
    body = """
            <!DOCTYPE html>
            <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width,initial-scale=1">
            <meta name="x-apple-disable-message-reformatting">
            <title>Tripbuddy password assitance</title>
            <style>
                body {
                    font-family: Arial, Helvetica, sans-serif;
                }
                .brand a{
                    font-size: 24px;
                    font-weight: 800;
                    letter-spacing: 1px;
                    cursor: pointer;
                    font-family: 'Poppins', sans-serif;
                    color: #fe4220;
                    float: inline-start;
                }
                .brand span{
                    margin: 10px;
                    float: right;
                }
                .content {
                    margin-left: 10px;
                }
            </style>
            </head>
            <body>
                <div class="brand">
                    <a href="https://chetan3010.pythonanywhere.com/">TripBuddy</a>
                    <span>Password assitance</span>
                </div>
                <div class="content">
                    <hr>
                    <span>To authenticate, please use the following One Time Password (OTP):</span>
                    <h1>"""+str(OTP)+"""</h1>
                    <p>We hope to see you again soon.</p>
                </div>
            </body>
            </html>
        """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body,subtype='html')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    return OTP

def forget(request):
    if request.method == "POST":
        forgetemail = request.POST.get("emailid")
        try:
            user = get_object_or_404(User,email=forgetemail)
        except:
            m.error(request,"Account doesn't exist with this email!")
            return render(request,"forget.html")
        if user is not None:
            try:
                checkExistUser = get_object_or_404(UserOtp,user=user)
            except:
                print("Except occured!")
            else:
                checkExistUser.delete()
            finally:
                f = UserOtp()
                f.user = user
                f.otp = generateOTP(request,forgetemail)
                f.save()

            return redirect("account:forget-verify",forgetemail)
        else:
            pass
    else:
        return render(request,"forget.html")

def forget_verify(request,forgetemail):
    if request.method == "POST":
        try:
            user = get_object_or_404(User,email=forgetemail)
        except:
            m.error(request,"Account doesn't exist with this email!")
            return redirect("account:forget-verify",forgetemail)
        otp = request.POST.get("otp")

        try:
            fverify = get_object_or_404(UserOtp,user=user,otp=otp)
        except:
            m.error(request,"The One Time Password (OTP) you entered is not valid. Please try again.")
            return redirect("account:forget-verify",forgetemail) 
        fverify.delete()
        return redirect("account:change-password",forgetemail)
    else:
        try:
            user = get_object_or_404(User,email=forgetemail)
        except:
            return redirect("account:forget")
        context = { 'femail':forgetemail,'username':user.username }
        return render(request,"forget-verify.html",context)

def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer



def change_password(request,forgetemail):
    if not get_referer(request):
        raise Http404
    else:
        if request.method == "POST":
            pass1 = request.POST.get("password1")
            pass2 = request.POST.get("password2")
            if pass1 != pass2:
                m.error(request,"Passwords do no match.")
                return redirect("account:change-password",forgetemail)
            else:
                f = User.objects.get(email=forgetemail)
                username = f.username
                f.set_password(pass1)
                f.save()
                m.success(request,"Login with your new password "+username+".")
                return redirect("account:signup_signin")
        else:
            f = ChangePasswordForm
            context = { 'changepass':ChangePasswordForm }
            return render(request,"change-password.html",context)

@login_required(login_url="account:signup_signin")
def addAdmin(request):
    if request.method == "POST":
        f=SignupForm(request.POST)  
        if f.is_valid():
            f.save()
            username = f.cleaned_data['username']
            uid = User.objects.get(username=username)
            uid.user_permissions.add(25,26,27,28,29,30,31,32)
            m.success(request, 'Admin account created successfully.')
            return render(request,"add-admin.html")
        else:
            try:
                f.save()
            except Exception as e:   
                m.error(request,e)
            return render(request,"add-admin.html")
    else:
        return render(request,"add-admin.html")