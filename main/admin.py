from django.contrib import admin
from .models import blog,Comment,Profile
# Register your models here.
admin.site.register(blog)
admin.site.register(Comment)
admin.site.register(Profile)