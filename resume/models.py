from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here.
class Resume(models.Model):
    file = models.FileField(upload_to='files/')
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)