from django.contrib import admin

# Register your models here.

from .models import Application, Article

admin.site.register(Application)
admin.site.register(Article)

