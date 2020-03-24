from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .models import blog
from django.urls import reverse
# Create your views here.
def login(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request,username=username,password = password)
	if user is not None:
		auth_login(request,user)
		return HttpResponseRedirect(reverse("index"))
	return render(request,"login.html",{"message":"Invalid Credentials"})

def logout(request):
	auth_logout(request)
	return render(request,"login.html",{"message":"Successfully logged out"})


def index(request):
	if not request.user.is_authenticated:
    		return render(request,'login.html',{"message":None})
	context={
		'blogs':blog.objects.all(),
		'user':request.user,
	}
	return render(request,'index.html',context=context)
	