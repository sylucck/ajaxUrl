from django.db import models

# Create your models here.
class UrlModel(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)