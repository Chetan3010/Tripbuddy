from django.contrib import admin
from django.urls import path,include
from trips import views as v
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from trips.views import *

router = routers.DefaultRouter()
router.register('tripsapi',TripsRetrive)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index),
    path('trips/',include(("trips.urls",'trips'),namespace='trips')),
    path('account/',include(("account.urls",'account'),namespace='account')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('',include(router.urls))
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'trips.views.custom_404'