from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from awwardsApp.models import *

# Create your views here.

# @login_required(login_url='/accounts/login/')
def home(request):
    images = Project.objects.all()
    current_user = request.user
    user = Profile.objects.filter(user_id=current_user.id)

    return render(request, 'home.html',{'images': images, 'user':user})



def profile(request):
    current_user = request.user
    image = Project.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()

    context = {"image": image, "profile": profile}


    return render(request, 'profile.html',context)