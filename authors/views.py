from django.shortcuts import render,redirect
# from django.http import HttpResponse
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post
# Create your views here.

# def addAuthor(request):
#     if request.method=='POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('addauthor')
#     else:
#          author_form = forms.AuthorForm()
#     return render(request,'add_author.html', {'form':author_form})
#     # return HttpResponse("this is Add AUthor page")


def register(request):
    if request.method=='POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created Succesfully')
            return redirect('signup')
    else:
        register_form = forms.RegistrationForm()
    return render(request,'register.html', {'form':register_form,'type':'register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'Log In Succesfully')
                login(request,user)
                return redirect('signup')
            else:
                messages.warning(request,'Log In information is in correct')
                return redirect('signup')
    else:
        form = AuthenticationForm()
        return render(request,'register.html',{'form':form,'type':'Login'})


def Profile(request):
    data=Post.objects.filter(author=request.user)
    return render(request,'profile.html',{'data':data})

@login_required
def updateProfile(request):
    if request.method=='POST':
        profile_form = forms.ChangeUserData(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Account Created Succesfully')
            return redirect('profile')
    else:
        profile_form =forms.ChangeUserData(instance=request.user)
    return render(request,'updateprofile.html', {'form':profile_form,'type':'profile'})

def pass_change(request):
    if request.method=='POST':
        change_form =PasswordChangeForm(request.user,data=request.POST)
        if change_form.is_valid():
            change_form.save()
            messages.success(request,'Password Change Succesfully')
            update_session_auth_hash(request,change_form.user)
            return redirect('profile')
    else:
        change_form = PasswordChangeForm(user=request.user)
    return render(request,'passchange.html', {'form':change_form})

def user_logout(request):
    logout(request)
    return redirect('login')