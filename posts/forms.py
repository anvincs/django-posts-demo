from django import forms 
from . import models

class createPost(forms.ModelForm):

    # this class should always be named Meta
    # this class is used to define the metadata of the form
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'banner']