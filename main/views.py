from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .models import blog, Comment, Profile
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import BlogForm,UpdateProfile
from django.core.exceptions import PermissionDenied
# Create your views here.
@login_required(redirect_field_name='login')
def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.update()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UpdateProfile(instance=request.user)

    args['form'] = form
    return render(request, 'update_profile.html', args)

@login_required(redirect_field_name='login')
def edit(request,blog_id):
	myblog = get_object_or_404(blog,id=blog_id)
	if myblog.author==request.user:
		form = BlogForm(instance=myblog)
		if request.method=='POST':
			form = BlogForm(request.POST, request.FILES, instance=myblog)
			if form.is_valid():
				obj = form.save(commit=False)
				obj.author = request.user
				obj.create()
				if request.POST["submit"]=="Publish":
					obj.publish()
				form = BlogForm()
		context = {
			'form':form,
			'blog_id':blog_id 
			}
		return render(request,"edit.html",context)
	else:
		raise PermissionDenied

@login_required(redirect_field_name='login')
def publish(request,blog_id):
	myblog = get_object_or_404(blog,id=blog_id)
	if myblog.author==request.user:
		myblog.is_publish = not myblog.is_publish
		myblog.save()
	return HttpResponseRedirect(reverse("blogs",kwargs={"username":myblog.author.username}))	

@login_required(redirect_field_name='login')
def delete(request,blog_id):
	myblog = get_object_or_404(blog,id=blog_id)
	if myblog.author==request.user:
		myblog.delete()
	return HttpResponseRedirect(reverse("blogs",kwargs={"username":myblog.author.username}))	


@login_required(redirect_field_name='login')
def Clap(request, blog_id):
	myblog = blog.objects.get(id=blog_id)
	clapper= request.user
	if clapper in myblog.claps.all():
		myblog.claps.remove(clapper)
		return HttpResponse("unclap")
	myblog.claps.add(clapper)
	return HttpResponse("Success")


@login_required(redirect_field_name='login')
def comment(request, blog_id):
	c = request.POST.get('comment', False)
	print(request.POST.keys(),c)
	post = get_object_or_404(blog, id=blog_id)
	if c!="":
		mycomment = Comment(post = post, commentator = request.user, text = c, created_date=timezone.now())
		mycomment.save()
	return HttpResponse("success")
	return HttpResponseRedirect(reverse("detail",kwargs={"id":blog_id}))

@login_required(redirect_field_name='login')
def follow(request,username):
	user = get_object_or_404(User,username=username)
	print()
	userprofile = user.profile
	follower = request.user
	followerprofile = follower.profile
	if follower in userprofile.follower.all():
		userprofile.follower.remove(follower)
		return HttpResponse("unfollow")
	userprofile.follower.add(follower)
	return HttpResponse("Success")


def userprofile(request,username):
	user = get_object_or_404(User,username=username)
	context = {
		"userprofile": user,
		}
	return render(request,"profile.html",context=context)

def view_details(request,id):
	context = {
		"blog":get_object_or_404(blog, id=id),
		"user":request.user,
		}
	return render(request,"view.html",context=context)

def blogswritten(request,username):
	user = get_object_or_404(User,username=username)
	MyBlogs = blog.objects.filter(author = user)
	context ={
		"user":user,
		"blogs":MyBlogs[::-1],
	}
	return render(request,'myblogs.html',context=context)

def register(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse("index"))
	try:
		username = request.POST["username"]
		password = request.POST["password"]
		email = request.POST["email"]
		name = request.POST["fullname"]
		user = User.objects.create_user(username,email,password)
		user.first_name = name
		user.save()
		if user is not None:
			auth_login(request,user)
			return HttpResponseRedirect(reverse("index"))
		return render(request,"register.html",{"message":"Unable to register"})
	except Exception as e:
		print(e)
		return render(request,"register.html",{"message":None})


def login(request):
	try:
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request,username=username,password = password)
		if user is not None:
			auth_login(request,user)
			return HttpResponseRedirect(reverse("index"))
		return render(request,"login.html",{"message":"Invalid Credentials"})
	except Exception as e:
		return render(request,"login.html",{"message":None})

@login_required(redirect_field_name='login')
def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse("index"))

@login_required(redirect_field_name='login')
def post_blog(request):
	form = BlogForm()
	if request.method=='POST':
		form = BlogForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.author = request.user
			obj.create()
			if request.POST["submit"]=="Publish":
				obj.publish()
			form = BlogForm()
	
	context = {
		'form':form 
	}
	return render(request,"post.html",context)
	

def index(request):
	user = request.user
	if not request.user.is_authenticated:
		user = None
	context={
		'blogs':blog.objects.filter(is_publish=True), 
		'user':user,
	}
	return render(request,'index.html',context=context)
	