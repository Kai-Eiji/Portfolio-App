# Generated by Django 3.0.6 on 2020-05-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projects_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.FilePathField(path='projects/img'),
        ),
    ]