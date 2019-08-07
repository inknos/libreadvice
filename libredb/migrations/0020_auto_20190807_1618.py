# Generated by Django 2.2.4 on 2019-08-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libredb', '0019_auto_20190803_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='pill',
            name='pil_image_url',
            field=models.CharField(blank=True, default='https://', max_length=200),
        ),
        migrations.AddField(
            model_name='pill',
            name='pil_short',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='app_description',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_abstract',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_description',
            field=models.CharField(blank=True, default='', max_length=280),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_link',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_subtitle',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='pill',
            name='pil_text',
            field=models.CharField(blank=True, default='', max_length=280),
        ),
    ]