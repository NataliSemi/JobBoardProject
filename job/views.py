from django.shortcuts import render

from .models import Job

# Create your views here.
def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)

    return render(request, 'job/detail.html', {'job':job})