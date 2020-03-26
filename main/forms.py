from django import forms
from .models import blog

class BlogForm(forms.Form):
    class Meta:
        model = blog
        fields = [
            'title',
            'description',

        ]
    
