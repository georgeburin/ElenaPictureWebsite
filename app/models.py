from django.db import models

# Create your models here.
class Picture(models.Model):
  name = models.CharField(max_length=1024)
  image = models.ImageField(null=True, blank=True)#no need to specify where it is saved