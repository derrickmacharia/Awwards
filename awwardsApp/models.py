from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500,  null=True)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def create_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    def __str__(self):
        return self.user.username

class Project(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images', null=True)
    image = CloudinaryField('image')
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    url = models.URLField(max_length=100, null=True)
    post_date = models.DateTimeField(auto_now_add=True,null=True)
    # rating =  models.ForeignKey(null=True,on_delete=CASCADE)
    # avg_rating = models

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


# rating models
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.IntegerField(default=0, blank=True, null=True)
    usability = models.IntegerField(default=0, blank=True, null=True)
    content = models.IntegerField(default=0, blank=True, null=True)
    average = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

    def save_ratw(self):
        self.save()

    def delete_rate(self):
        self.delete()

    @classmethod
    def get_project_rates(cls, project):
        return cls.objects.filter(project = project)
