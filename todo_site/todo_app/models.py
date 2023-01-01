from django.db import models

# Create your models here.
# This is what creates the structure of our DB

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    ''' Connects to the Task model --> to connect our tables together '''



class Task(models.Model):
    ''' A task object wil have a description of the task to complete '''
    description = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    ''' The ManyToManyField: This connects our two tables '''


class Comment(models.Model):
    '''A Comment will be created -  ID will be set for us'''
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE) 
    ''' Cascasde is in reference to how SQL handles a deleted task'''
