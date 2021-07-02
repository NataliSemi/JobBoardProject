from django import forms
from .models import Job, Application



class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'categories', 'short_description', 'long_description', 'company_name', 'company_place', 'company_country', 'tags']
        

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']


class SearchJob(forms.Form):
    query = forms.CharField()
