from django.db import models

# Create your models here.
# This is what creates the structure of our DB
class Task(models.Model):
    description = models.CharField(max_length=255)
