from django.contrib import admin
from .models import *
# Register your models here.
class TripsAdmin(admin.ModelAdmin):
    list_display = ['id','trip_name','trip_type','trip_sublocation','trip_location','trip_country','trip_rating','trip_image']

admin.site.register(trips,TripsAdmin)

class TripsImagesAdmin(admin.ModelAdmin):
    list_display = ['id','trip_id','images']

admin.site.register(Trips_images,TripsImagesAdmin)
