from django.contrib import admin
from django.urls import path,re_path
from . import views as main_views
from awwardsApp import views

urlpatterns=[
    path('',views.home,name = 'index'),
    path('profile/',views.profile,name = 'profile'),
    path('project/', views.upload, name = "upload"),
    path("project/<int:project_id>/", views.project_details, name="project_details"),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('search/', views.search_project, name='search.post'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
]