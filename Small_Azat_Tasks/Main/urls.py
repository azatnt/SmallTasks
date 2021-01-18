from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
from User.views import *


urlpatterns = [

    path('', index, name='index_url'),
    path('register/', register, name='register_url'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html', authentication_form=MyAuthForm), name='login_url'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout_url'),
    path('profile/', profiles, name='profile_url'),

]
