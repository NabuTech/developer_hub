# profiles/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Skill, Profile

class ProfileModelTestCase(TestCase):
    def setUp(self):
        # Create a user and skills for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.skill1 = Skill.objects.create(name='Python')
        self.skill2 = Skill.objects.create(name='Django')
        self.skill3 = Skill.objects.create(name='JavaScript')

    def test_profile_creation(self):
        # Test if a profile is created when a user is created
        profile = Profile.objects.create(user=self.user)
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.skills.count(), 0)
        self.assertEqual(profile.expertise.count(), 0)
        self.assertEqual(profile.preferred_languages.count(), 0)

    def test_skill_relationships(self):
        # Test if skills can be added to a profile
        profile = Profile.objects.create(user=self.user)
        profile.skills.add(self.skill1, self.skill2)
        profile.expertise.add(self.skill2)
        profile.preferred_languages.add(self.skill3)

        self.assertEqual(profile.skills.count(), 2)
        self.assertEqual(profile.expertise.count(), 1)
        self.assertEqual(profile.preferred_languages.count(), 1)

    def test_str_method(self):
        # Test the __str__ method of the Profile model
        profile = Profile.objects.create(user=self.user)
        self.assertEqual(str(profile), 'testuser')
