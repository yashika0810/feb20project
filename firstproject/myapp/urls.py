from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('welcome', views.home ),

    path('register', views.form_view, name= 'register'), 
    path('home', views.home, name='home'),

]


