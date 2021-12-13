from typing import Callable
from django.contrib import admin
from .models import Category, Location, Profile, Project, Rating

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Rating)
