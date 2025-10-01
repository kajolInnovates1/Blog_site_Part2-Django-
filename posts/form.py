from django import forms
from .models import Post
class addpost(forms.ModelForm):
    class Meta:
        model=Post
        # fields='__all__'
        exclude = ['author']