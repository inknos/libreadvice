import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# TODO insert help_text to see grey text to describe fields

class Application(models.Model):
    app_full_name = models.CharField(max_length=200)
    app_description = models.CharField(
        max_length=400,
        default="",
        blank=True
    )
    app_link = models.URLField(
        max_length=200,
        default="https://",
        blank=True
    )

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
        return self.app_full_name

class Article(models.Model):
    art_app_name = models.CharField(max_length=200) # Name of the app: must be in the db
    art_title = models.CharField(max_length=200) # Name of the article
    art_subtitle = models.CharField( # Single phrase to catch the attention
        max_length=200,
        default="",
        blank=True,
    )
    art_abstract = models.CharField( # Single paragraph to introduce and sum up
        max_length=500,
        default="",
        blank=True,
    )
    art_description = models.CharField( # Post-like description
        max_length=280,
        default="",
        blank=True,
    )
    art_link = models.URLField( # link to the article in libreadvice.org
        max_length=200,
        default="",
        blank=True
    )
    ART_STATE_CHOICE = [
        ('TO', 'TODO'),             # Just a concept
        ('WP', 'Work In Progress'), # Started, link created
        ('DR', 'Drafted'),          # Title created, subtitle, ...
        ('RW', 'Review'),           # Finished it needs correction
        ('TP', 'To Publish'),       # Ready to go online
        ('PU', 'Published'),        #
    ]
    art_state = models.CharField(
        max_length=2,
        choices=ART_STATE_CHOICE,
        default='TO'
    )

    def __str__(self):
        return self.art_title

class Pill(models.Model):
    pil_app_name = models.CharField(max_length=200)
    pil_name = models.CharField(max_length=200)
    pil_text = models.CharField(
        max_length=280,
        default="",
        blank=True,
    )
    pil_short = models.CharField(max_length=200, default="", blank=True)
    PIL_STATE_CHOICE = [
        ('TO', 'TODO'),             # Just a concept
        ('WP', 'Work In Progress'), # Started, link created
        ('DR', 'Drafted'),          # Title created, subtitle, ...
        ('RW', 'Review'),           # Finished it needs correction
        ('TP', 'To Publish'),       # Ready to go online
        ('PU', 'Published'),        #
    ]
    pil_state = models.CharField(
        max_length=2,
        choices=PIL_STATE_CHOICE,
        default='TO',
    )
    pil_image_url = models.CharField(max_length=200, default="https://", blank=True)
    def __str__(self):
        return self.pil_name
