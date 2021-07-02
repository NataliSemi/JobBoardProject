from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from taggit.models import Tag
from job.models import Job


def frontpage(request, tag_slug=None):
    job = Job.published.all()
    employed = Job.employed.all()
    archived = Job.archived.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        job = job.filter(tags__in=[tag])

    paginator = Paginator(job, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        jobs = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'core/frontpage.html', {'page': page,
                                                    'jobs': jobs,
                                                    'tag': tag,
                                                    'employed': employed,
                                                    'archived': archived})



