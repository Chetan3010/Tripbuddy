from django.db import models

# Create your models here.

class trips(models.Model):
    trip_name = models.CharField(max_length=100)
    trip_type = models.CharField(max_length=100)
    trip_description = models.TextField()
    trip_sublocation = models.CharField(max_length=50)
    trip_location = models.CharField(max_length=50)
    trip_country = models.CharField(max_length=100)
    trip_cost = models.IntegerField(default="999999")
    trip_rating = models.IntegerField(default=0)
    trip_image = models.ImageField(upload_to="images/",default="")
    
    class Meta:
        db_table = 'trips'

    def __str__(self):
        return self.trip_name
    
class Trips_images(models.Model):
    trip_id = models.ForeignKey(trips,on_delete=models.CASCADE)
    images = models.ImageField(upload_to="images/",default="")

    class Meta:
        db_table = 'trips_images'