from django.shortcuts import render
from django.http import HttpResponse
from .models import blog
# Create your views here.
def login(request):
	context={
		'blogs':blog.objects.all()
	}
	return render(request,'index.html',context=context)