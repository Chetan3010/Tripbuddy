from django.contrib import admin
from .models import *
# Register your models here.

class BookingsAdmin(admin.ModelAdmin):
    list_display = ['BK_Name','BK_Phone','BK_Email','BK_time','BK_travel_date','BK_No_of_travelers','BK_uid','BK_trip_id','BK_Status','BK_Cancel']

class UserPfpAdmin(admin.ModelAdmin):
    list_display = ['user','profile_pic']

admin.site.register(Bookings,BookingsAdmin)
admin.site.register(UserPfp,UserPfpAdmin)