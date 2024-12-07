from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
#This file maps urls to views
