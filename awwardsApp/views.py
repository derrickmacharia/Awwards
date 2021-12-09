from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from awwardsApp.models import *

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()

    return render(request, 'home.html',{'images': images})
