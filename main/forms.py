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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    
class ProfileForm(forms.Form):
    pass
    
    


