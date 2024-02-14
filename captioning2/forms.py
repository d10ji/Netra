from django import forms
from captioning2.models import image
from django.forms import ModelForm


class image_form(forms.ModelForm):


    class Meta:
        model=image
        fields=['IMAGE']
