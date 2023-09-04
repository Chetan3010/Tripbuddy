from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
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

# FOR DEBUG True
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# New config for debug false
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]

handler404 = 'trips.views.custom_404'