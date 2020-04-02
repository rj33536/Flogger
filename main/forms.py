from django import forms
from .models import blog, Profile
from django.contrib.auth.models import User
class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = [
            'title',
            'description',
            'text',
            'image'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    
class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def update(self, commit=True):
        user = self.save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user 
    


