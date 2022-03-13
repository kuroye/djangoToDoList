from django import forms
from .models import *

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        # fields = ['name', 'description', 'grade', 'requirement', 'image']
        fields = ['image']
