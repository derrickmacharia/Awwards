from django.contrib import admin
from django.urls import path,re_path
from . import views as main_views
from awwardsApp import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('profile/',views.profile,name = 'profiles'),
]