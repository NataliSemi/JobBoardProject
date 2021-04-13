from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    show_description = models.TextField()
    long_description = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, related_name='jobs')