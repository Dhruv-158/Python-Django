from django.contrib import admin
from django.urls import path
from Home import views 

urlpatterns = [
    path("", views.home,name="Home"),
    path("about",views.about,name="about"),
    path("Blog",views.Blog,name="Blog"),
    path("contect",views.contect,name="contect"),
    path("signin",views.signin_view,name="signin"),
    path("login",views.login_view,name="login"),
    path("Profile",views.Profile,name="Profile"),
    path("logout",views.logout_view,name="logout"),
    # path("form",views.form,name="form"),
    path('newsdetails/<int:id>/',views.newsdetail,name="newsdetail")
]
