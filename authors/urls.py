from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.register,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_login,name='logout'),
    path('profile/',views.Profile,name='profile'),
    path('profile/updateprofile/',views.updateProfile,name='updateprofile'),
    path('profile/changepass/',views.pass_change,name='changepass')    
 
    
]
