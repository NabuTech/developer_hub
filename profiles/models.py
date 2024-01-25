
from django.db import models
from django.conf import settings

class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    expertise = models.ManyToManyField(Skill)
    preferred_languages = models.ManyToManyField(Skill)

    def __str__(self):
        return self.user.username