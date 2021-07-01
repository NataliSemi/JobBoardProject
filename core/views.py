from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger

from job.models import Job

from userprofile.models import Userprofile


def frontpage(request):
    job = Job.published.all()
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

    return render(request, 'core/frontpage.html', {'job':job,
                                                    'jobs':jobs,
                                                    'page':page})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'jobseeker')

            if account_type == 'employer':
                userprofile = Userprofile.objects.create(user=user, is_employer=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()

            login(request, user)

            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})
