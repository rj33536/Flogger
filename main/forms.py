from django import forms
from .models import blog, Profile

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = [
            'title',
            'text',
            'image'
        ]
    
class ProfileForm(forms.Form):
    pass
    
    


