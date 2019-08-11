#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Application, Article, Pill

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ['app_full_name', 'app_description', 'app_link']

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['art_title', 'art_abstract', 'art_link']

class PillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pill
        fields = ['pil_name', 'pil_text', 'pil_short', 'pil_state']
