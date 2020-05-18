from django.db import models

# Create your models here.

class Signuser(models.Model):
    username = models.CharField(max_length=50)
    stamp = models.ImageField(upload_to="signatures")
