from django.urls import path,include
from . import views
urlpatterns = [
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('',views.index,name="index"),
    path('post',views.post_blog,name="post"),
    path('view/<int:id>',views.view_details,name="detail"),
    path('myblogs',views.myblogs, name="myblogs"),
    path('register',views.register,name="register")
]
