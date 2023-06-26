from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from account import views as v

urlpatterns = [
    path('signup-signin',v.signup_signin,name='signup_signin'),
    path('signup',v.signup,name='signup'),
    path('signin',v.signin,name='signin'),
    path('signout',v.signout,name='signout'),
    path('bookings/<int:id>',v.booknow,name="bookings"),
    path('mybookings',v.mybookings,name="mybookings"),
    path('cancel-booking/<int:id>',v.cancel,name="cancel"),
    path('edit-profile',v.editprofile,name="edit-profile"),
    path('add-trip-img',v.addtripimg,name="addtripimg"),
    path('add-trip',v.addtrip,name="addtrip"),
    path('triplist',v.triplist,name="triplist"),
    path('tripupdate/<int:id>',v.tripup,name="tripup"),
    path('tripdel/<int:id>',v.tripdel,name="tripdel"),
    # path('webhook',v.webhook),
]
