from django.forms import ModelForm
from django import forms
from .models import *

class ArtForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title1', 'title2', 'subtitle', 'art']