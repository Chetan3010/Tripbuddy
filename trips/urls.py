from django.urls import path
from trips import views as v
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('all/',v.trip_search,name="trip_search"),
    path('trip_detail/<int:id>',v.trip_detail,name="trip_detail"),
    path('all/<str:trip_type>/<str:trip_country>',v.trip_list,name="filter_trips"),
]
