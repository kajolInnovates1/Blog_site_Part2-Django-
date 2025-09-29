from django.urls import path
from . import views
urlpatterns = [
    path('addauthor/',views.addAuthor,name='addauthor')
    
]
