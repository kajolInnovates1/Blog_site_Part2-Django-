from django.shortcuts import render,redirect
# from django.http import HttpResponse
from . import forms
# Create your views here.

def addAuthor(request):
    if request.method=='POST':
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('addauthor')
    else:
         author_form = forms.AuthorForm()
    return render(request,'add_author.html', {'form':author_form})
    # return HttpResponse("this is Add AUthor page")
