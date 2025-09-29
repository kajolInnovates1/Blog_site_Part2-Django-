from django.urls import path
from . import views
urlpatterns = [
    path('addcategory/',views.addCategory,name='addcategory')
]
