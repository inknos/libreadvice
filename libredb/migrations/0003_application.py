# Generated by Django 2.2.4 on 2019-08-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libredb', '0002_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=200)),
            ],
        ),
    ]
