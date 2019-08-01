from django.contrib import admin

# Register your models here.

from .models import Application, Articles

admin.site.register(Application)
admin.site.register(Articles)

