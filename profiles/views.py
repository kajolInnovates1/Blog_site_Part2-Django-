from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import ProfileForm

# Create your views here.

def addProfile(request):
    if request.method=='POST':
        profile =ProfileForm(request.POST)
        if profile.is_valid():
            profile.save()
            return redirect('addprofile')
    else:
        profile =ProfileForm()



    
    return render(request,'add_profile.html',{"form":profile})
