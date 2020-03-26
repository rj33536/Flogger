from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('accounts/login/',views.login,name="login"),
    path('accounts/logout/',views.logout,name="logout"),
    path('',views.index,name="index"),
    path('post',views.post_blog,name="post"),
    path('view/<int:id>',views.view_details,name="detail"),
    path('myblogs',views.myblogs, name="myblogs"),
    path('register',views.register,name="register"),
    path('clap/<int:blog_id>',views.Clap,name="clap"),
    path('users/<str:username>',views.userprofile, name="profile"),

] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
