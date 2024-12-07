"""
URL configuration for HannahsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from FastRunners import views
from FastRunners.views import register, CustomLoginView

urlpatterns = [
path('admin/', admin.site.urls),

 path('', include('FastRunners.urls')),
 path('', views.home,name='home'),
 path('cars/', views.car_list, name='car_list'),
 path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
 path('about-us/', views.about_us, name='about_us'),
 path('contact-us/', views.contact_us, name='contact_us'),

 path('register/', views.register, name='register'),

path('login/', CustomLoginView.as_view(), name='login'),
path('logout/', LogoutView.as_view(next_page='home'), name='logout')



]


