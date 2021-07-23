from django.urls import path,include

from .views import home,error404,error500,loginn,register,logout,profile,product




urlpatterns = [
    path('',home,name="home"),
    path('404',error404,name="error404"),
    path('500',error500,name="error500"),
    path('login',loginn,name="login"),
    path('logout',logout,name="logout"),
    path('register',register,name="register"),
    path('profile',profile,name="profile"),
    path('enterProduct',product,name="enter-product"),
]
