# Generated by Django 3.0.6 on 2020-05-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200518_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='git',
            field=models.URLField(default='default_link'),
        ),
    ]
