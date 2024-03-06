from django.db import models

# Create your models here.
from django.db import models


class Training(models.Model):
    title = models.CharField(max_length=20)
    describe = models.CharField(max_length=200)
    #date_time = models.DateTimeField()
    #logo = models.ImageField(upload_to='logotypes')