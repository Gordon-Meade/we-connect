# from django_summernote.fields import SummernoteTextField
from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    max_participation = models.PositiveIntegerField(blank=True, null=True)
    event_type = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return self.title