from django import forms
from .models import Job

class AddJobForm(models.Model):
    class Meta:
        model = Job
        fields = ['title', 'short_description', 'long_description'] 