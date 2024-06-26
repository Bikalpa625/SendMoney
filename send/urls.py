"""
URL configuration for send project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_view
from sendmoney import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',user_views.logoutuser, name='logout'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password_reset"),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete"),
    path('sendmoney/',include('sendmoney.urls')),
    path('send_money/',views.send_money, name='send_money'),
    path('homepage/', views.homepage, name='homepage'),
    path('about_us/', views.about_us, name='about_us'),
    path('track-transfer/', views.track_transfer,name='track_transfer'),
    
    path('contact/', views.contact,name='contact'),
]
