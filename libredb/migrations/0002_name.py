# Generated by Django 2.2.4 on 2019-08-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libredb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
            ],
        ),
    ]