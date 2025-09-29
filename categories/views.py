from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import addcategory
# Create your views here.

def addCategory(request):
    if request.method=='POST':
        category = addcategory(request.POST)
        if category.is_valid():
            category.save()
            return redirect('addcategory')
    else:
        category = addcategory()


    
    return render(request,'addCategory.html',{'form':category})
