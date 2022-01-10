from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from awwardsApp.forms import *
from django.contrib.auth.models import User
from awwardsApp.models import *
from django import forms
from django.http.response import Http404, HttpResponseRedirect
import cloudinary
import cloudinary.uploader
import cloudinary.api
from awwardsApp.models import Profile
from rest_framework import serializers
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from awwardsApp import serializer
from django.http import HttpResponseRedirect, Http404
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework.response import Response


# Create your views here.

# @login_required(login_url='/accounts/login/')
# def home(request):
#     images = Project.objects.all().order_by('-id')

#     return render(request, 'home.html',{'images': images})


@login_required(login_url="/accounts/login/")
def home(request):
    current_user = request.user
    images = Project.objects.all().order_by('-id')
    user = Profile.objects.all()

    return render(request, 'home.html', {'images':images, 'user':user, 'current_user':current_user})



# def details(request, project_id):
#     images = Project.objects.get(id=project_id)

#     return render(request, 'project_details.html', {'images':images})


def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    # get project rating
    rating = Rating.objects.filter(project=project)
    return render(request, "project_details.html", {"project": project, 'rating':rating})

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id).all() 

    return render(request, "profile.html", {"profile": profile, "project": project})

@login_required(login_url="/accounts/login/")
def upload(request):
    if request.method =='POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect('/')
    else:
        form =  ProjectForm()
    return render(request, 'project.html', {'form':form})

@login_required(login_url='/accounts/login/')
def search_project(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        images = Project.search_project_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'found': message, 'images': images})
    else:
        message = 'Not found'
        return render(request, 'search.html', {'danger': message})

@login_required(login_url="/accounts/login/")
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})

@login_required(login_url="/accounts/login/")
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx)

@login_required(login_url="/accounts/login/")
def rating(request,id):
    if request.method == 'POST':
        project = Project.objects.get(id = id)
        current_user = request.user
        design = request.POST['design']
        content = request.POST['content']
        usability = request.POST['content']

        Rating.objects.create(
            project=project,
            user=current_user,
            design=design,
            usability=usability,
            content=content,
            average=round((float(design)+float(usability)+float(content))/3,2),)

        return render(request, 'project_details.html',{'project':project})

    else:
        project = Project.objects.get(id = id)
        return render(request, 'project_details.html',{'project':project})

class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects,many=True)
        return Response(serializer.data)

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles,many=True)
        return Response(serializer.data)