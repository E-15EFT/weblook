# from unicodedata import name
from django.db import models

# Create your models here.
class video(models.Model):
    Moviesname=models.CharField(max_length=100)
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption

 
