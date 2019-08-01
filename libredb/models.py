import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Application(models.Model):
    app_name = models.CharField(max_length=200)
    app_description = models.CharField(max_length=400)
    app_link = models.URLField(max_length=200)

    APP_GRADE_CHOICES = [
        ('1', 'Terrible'),
        ('2', 'Mediocre'),
        ('3', 'Discrete'),
        ('4', 'Good'),
        ('5', 'Excellent')
    ]
    app_libre = models.CharField(
        max_length=1,
        choices=APP_GRADE_CHOICES,
        default='3',
    )
    app_usability = models.CharField(
        max_length=1,
        choices=APP_GRADE_CHOICES,
        default='3',
    )
    app_porting = models.CharField(
        max_length=1,
        choices=APP_GRADE_CHOICES,
        default='3',
    )
    app_potential = models.CharField(
        max_length=1,
        choices=APP_GRADE_CHOICES,
        default='3',
    )
    app_design = models.CharField(
        max_length=1,
        choices=APP_GRADE_CHOICES,
        default='3',
    )
    app_ethic = models.BooleanField(default=False)
    app_used_for_libreadvice = models.BooleanField(default=False)
    def __str__(self):
        return self.app_name

class Article(models.Model):
    art_app_name = models.CharField(max_length=200)
    art_title = models.CharField(max_length=200)
    art_link = models.URLField(max_length=200)
    art_written = models.BooleanField(default=False)
    art_published = models.BooleanField(default=False)

    def __str__(self):
        return self.art_title

class Pills(models.Model):
    pil_name = models.CharField(max_length=200)
    pil_text = models.CharField(max_length=280)
    pil_published = models.BooleanField(default=False)

    def __str__(self):
        return self.pil_name
