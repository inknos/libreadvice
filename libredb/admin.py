from django.contrib import admin

# Register your models here.

from .models import Application, Article, Pill

admin.site.register(Application)
admin.site.register(Article)
admin.site.register(Pill)
