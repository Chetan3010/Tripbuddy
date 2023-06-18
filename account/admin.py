from django.contrib import admin
from .models import *
# Register your models here.

class BookingsAdmin(admin.ModelAdmin):
    list_display = ['BK_Name','BK_Phone','BK_Email','BK_travel_date','BK_No_of_travelers','BK_uid','BK_trip_id','BK_Status','BK_Cancel']

admin.site.register(Bookings,BookingsAdmin)