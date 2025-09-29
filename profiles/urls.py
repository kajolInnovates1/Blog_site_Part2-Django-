from django.urls import path,include
from . import views

urlpatterns = [
    path('addprofile/',views.addProfile,name='addprofile')
]
