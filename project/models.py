from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    language = models.CharField(max_length=50)

    link = models.URLField()
    image = models.ImageField(upload_to='profile/projects', blank=True)