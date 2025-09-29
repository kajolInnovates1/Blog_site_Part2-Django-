from django.urls import path
from . import views
urlpatterns = [
    path('addpost/',views.addPost,name='addpost'),
    path('editpost/<int:id>',views.editPost,name='editpost'),
    path('delete_post/<int:id>',views.delete_post,name='delete_post')
]
