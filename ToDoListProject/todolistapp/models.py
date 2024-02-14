# models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255, default='Default Title')
    description = models.TextField()


def __str__(self):
        return self.title

