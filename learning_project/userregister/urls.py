from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from userregister import views as user_views

#same functions as post.urls
urlpatterns=[
    path('register/',views.register,name='User-Register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile')
]
