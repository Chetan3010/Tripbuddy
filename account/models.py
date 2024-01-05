from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from trips.models import *
from django.utils import timezone
from datetime import date

# Storing user social profile picture
class UserPfp(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   profile_pic = models.TextField(null=True, blank=True)

# Storing user bookings
class Bookings(models.Model):
    BK_Name = models.CharField(max_length=100)
    BK_Phone = models.PositiveIntegerField()
    BK_Email = models.EmailField(max_length=30)
    BK_AadharNo = models.IntegerField()
    BK_travel_date = models.DateField()
    BK_No_of_travelers = models.PositiveIntegerField(default=0)
    BK_uid = models.ForeignKey(User,on_delete=models.CASCADE)
    BK_trip_id = models.ForeignKey(trips,on_delete=models.CASCADE)
    BK_time = models.DateTimeField()
    BK_Status = models.BooleanField(default=0)
    BK_Cancel = models.BooleanField(default=0)

    class Meta:
        db_table = 'Bookings'

    def bookingTimeValidation(self):
        if( timezone.localtime() <= self.BK_time + timezone.timedelta(days=1)):
            return True
        return False
    
    def bookingDateValidation(self):
        if( self.BK_travel_date < date.today()):
            return True
        return False

# Storing otp to verification
class UserOtp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    otp = models.IntegerField()
    class Meta:
        db_table = 'UserOtp'


# Storing sub travellers details
# Its under development so not available right now!
class BookingsSubTravellers(models.Model):
    BK_Id = models.ForeignKey(Bookings,on_delete=models.CASCADE)
    BKST_Name = models.CharField(max_length=100)
    BKST_Phone = models.PositiveIntegerField()
    BKST_Email = models.EmailField(max_length=30)
    
    class Meta:
        db_table = 'BookingsSubTravellers'





# ---------------- FORMS ----------------
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = "__all__"
        
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class TripsForm(forms.ModelForm):
    class Meta:
        model = trips
        fields = ['trip_name','trip_type','trip_description','trip_sublocation','trip_country','trip_cost','trip_rating','trip_image']

class TripsImagesForm(forms.ModelForm):
    class Meta:
        model = Trips_images
        fields = "__all__"

class UserOtpForm(forms.ModelForm):
    class Meta:
        model = UserOtp
        fields = "__all__"

class ChangePasswordForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password1','password2']