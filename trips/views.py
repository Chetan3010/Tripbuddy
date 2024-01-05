from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from account.views import signup_signin
from rest_framework import serializers,viewsets
from .serializer import *
from rest_framework.permissions import IsAdminUser,SAFE_METHODS,BasePermission
from django.views.decorators.cache import cache_control
from datetime import date,timedelta


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    india_images = trips.objects.filter(trip_country__icontains="india")
    maldives_images = trips.objects.filter(trip_country__icontains="maldives")
    norway_images = trips.objects.filter(trip_country__icontains="norway")
    china_images = trips.objects.filter(trip_country__icontains="china")
    switzerland_images = trips.objects.filter(trip_country__icontains="switzerland")
    uk_images = trips.objects.filter(trip_country__icontains="united kingdom")
    context = {'india_images':india_images,'maldives_images':maldives_images,'norway_images':norway_images,'china_images':china_images,'switzerland_images':switzerland_images,'uk_images':uk_images}
    return render(request,"index.html",context)

def custom_404(request, exception):
    return render(request, "error404.html", status=404)

def custom_500(request, *args, **argv):
    return render(request, "error500.html", status=500)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="account:signup_signin")
def trip_list(request,trip_type,trip_country):
    if trip_country == "world":
        data = trips.objects.filter(trip_type__icontains=trip_type)
    else:
        data = trips.objects.filter(trip_country__icontains=trip_country,trip_type__icontains=trip_type)
    context = {'filtered_trips':data,'trip_type':trip_type,'trip_country':trip_country}
    return render(request,"trips_list.html",context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="account:signup_signin")
def trip_detail(request,id):
    data = trips.objects.get(id=id)
    image_data = Trips_images.objects.filter(trip_id=id)
    nextDate = (date.today() + timedelta(1))
    context = {'trip_detail':data,'images':image_data,'nextDate':nextDate}
    return render(request,"details_page.html",context)


def trip_search(request):
    srch = request.POST.get("search-place")
    data = trips.objects.filter(
            Q(trip_name__icontains=srch) | Q(trip_location__icontains=srch) | Q(trip_sublocation__icontains=srch) | Q(trip_country__icontains=srch) | Q(trip_type__icontains=srch)
        )
    context = {'filtered_trips':data}
    return render(request,"trips_list.html",context)

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class TripsRetrive(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    serializer_class = TripsSerializer
    queryset = trips.objects.all()