# Generated by Django 2.2.4 on 2019-08-01 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libredb', '0004_auto_20190801_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_app_name', models.CharField(max_length=200)),
                ('art_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Name',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]