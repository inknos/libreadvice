import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Application(models.Model):
    app_name = models.CharField(max_length=200)
    app_description = models.CharField(max_length=400)
    app_link = models.URLField(max_length=200)

    def __str__(self):
        return self.app_name

class Articles(models.Model):
    art_app_name = models.CharField(max_length=200)
    art_title = models.CharField(max_length=200)

    def __str__(self):
        return self.art_title
