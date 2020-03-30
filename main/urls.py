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
    path('comment/<int:blog_id>',views.comment,name="comment"),
    path('users/<str:username>',views.userprofile, name="profile"),
    path('publish/<int:blog_id>',views.publish,name="publish"),
    path('delete/<int:blog_id>',views.delete,name="delete"),
    path('edit/<int:blog_id>', views.edit, name="edit")

] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
