from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=250)
    description = models.TextField()
    language = models.CharField(max_length=50)
    link = models.URLField()
    image = models.ImageField(upload_to='project/', blank=True)