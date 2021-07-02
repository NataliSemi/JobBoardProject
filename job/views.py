from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddJobForm, ApplicationForm,SearchJob
from .models import Job

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity

from notification.utilities import create_notification


# def search_job(request):
#     form = SearchJob()
#     query = None
#     search_vector = SearchVector('title', weight='A') + SearchVector('short_description', weight='B')
#     search_query = SearchQuery(query)
#     results = Job.published.annotate(
#         search=search_vector,
#         rank=SearchRank(search_vector, search_query)
#     ).filter(rank__gte=0.3).order_by('-rank')

#     if 'query' in request.GET:
#         form = SearchJob(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             results = Job.published.annotate(
#                 similarity=TrigramSimilarity('title', query),
#             ).filter(similarity__gt=0.1)
#     return render(request, 'job/search.html', {'form': form,
#                                                      'query': query,
#                                                      'results': results})



def job_detail(request, year, month, day, job):
    job = get_object_or_404(Job, id=job,
                            status="ACTIVE",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)


    return render(request, 'job/job_detail.html', {'job': job})


@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job,pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            create_notification(request, job.created_by, 'application', extra_id=application.id)

            return redirect('dashboard')
    else:
        form = ApplicationForm()

    return render(request, 'job/apply_for_job.html', {'form': form, 'job': job})


@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm()
    
    return render(request, 'job/add_job.html', {'form': form})



@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    if request.method == 'POST':
        form = AddJobForm(request.POST, instance=job)

        if form.is_valid():
            job = form.save(commit=False)
            job.status = request.POST.get('status')
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm(instance=job)
    
    return render(request, 'job/edit_job.html', {'form': form, 'job': job})