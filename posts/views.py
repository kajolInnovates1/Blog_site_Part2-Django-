from django.shortcuts import render,redirect
from .form import addpost
from posts.models import Post
# Create your views here.

def addPost(request):
    if request.method=='POST':
        forrm=addpost(request.POST)
        if forrm.is_valid():
            forrm.save()
            return redirect('addpost')
    else:
        forrm=addpost()

    return render(request,'post.html',{'form':forrm})

def editPost(request,id):
    post =Post.objects.get(pk=id)
    forrm=addpost(instance=post)

    if request.method=='POST':
        forrm=addpost(request.POST,instance=post)
        if forrm.is_valid():
            forrm.save()
            return redirect('home')
    

    return render(request,'post.html',{'form':forrm})
def delete_post(request,id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect('home')
