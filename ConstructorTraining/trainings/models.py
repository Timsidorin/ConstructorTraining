from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
class Training(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    describe = models.CharField(max_length=200)
    date_time = models.DateTimeField(default=timezone.now )
    logo = models.ImageField(upload_to='logotypes/')



class Coordinates(models.Model):
    top = models.CharField(max_length=50)
    left = models.CharField(max_length=50)
    width = models.CharField(max_length=50)
    height = models.CharField(max_length=50)