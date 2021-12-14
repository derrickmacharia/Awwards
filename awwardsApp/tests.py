from django.contrib.auth.models import User
from django.test import TestCase
from .models import  Profile


class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="test_user"
        )

        self.profile = Profile(
            bio="Test profile_photo",
            user=user,
            contact="Test Contact",
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_update_method(self):
        self.profile.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


