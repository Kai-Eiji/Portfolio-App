from django.db import models


# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    link = models.URLField(max_length=200, default='https://github.com/Kai-Eiji')
    git = models.URLField(max_length=200, default='https://github.com/Kai-Eiji')




