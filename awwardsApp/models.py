from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.fields import related

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name



class Project(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    post_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

        # delete image
    def delete_project(self):
        self.delete()

    @classmethod
    def get_project_by_user(cls, user):
        images = cls.objects.filter(user=user)
        return images

    def update_project(self, title, description):
        self.title = title
        self.description = description
        self.save()

    # get all images
    @classmethod
    def get_all_project(cls):
        today = dt.date.today()
        images = Project.objects.all(post_date__date = today)
        return images

    @classmethod
    def search_project_name(cls, search_term):
        images = cls.objects.filter(
        title__icontains=search_term)
        return images    

    def _str_(self):
        return self.user.username       

    @classmethod
    def get_single_project(cls, id):
        image = cls.objects.get(id=id)
        return image

    def _str_(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    

    def __str__(self):
        return self.user.username