# Generated by Django 2.2.4 on 2019-08-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libredb', '0016_auto_20190803_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='app_description',
            field=models.CharField(default='no description yet', max_length=400),
        ),
        migrations.AlterField(
            model_name='application',
            name='app_link',
            field=models.URLField(default='https://'),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_abstract',
            field=models.CharField(default='no abstract yet', max_length=500),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_description',
            field=models.CharField(default='no description yet', max_length=280),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_link',
            field=models.URLField(default='no link to article yet'),
        ),
        migrations.AlterField(
            model_name='article',
            name='art_subtitle',
            field=models.CharField(default='no subtitle yet', max_length=200),
        ),
        migrations.AlterField(
            model_name='pill',
            name='pil_text',
            field=models.CharField(default='no text yet', max_length=280),
        ),
    ]