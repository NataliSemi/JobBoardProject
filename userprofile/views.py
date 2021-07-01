from django.contrib.auth.decorators  import login_required
from django.shortcuts import render, redirect
from job.models import Application, Job
from django.shortcuts import get_object_or_404
from .models import ConversationMessage
from notification.utilities import create_notification
from django.contrib.auth.models import User
from userprofile.models import Userprofile


@login_required
def dashboard(request):
    return render(request, 'userprofile/dashboard.html', {'userprofile': request.user.userprofile})


@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)
    
    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(application=application, content=content, created_by=request.user)

            create_notification(request, application.created_by, 'message', extra_id=application.id)

            return redirect('view_application', application_id=application_id)
    
    return render(request, 'userprofile/view_application.html', {'application': application})


@login_required
def view_dashboard_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    return render(request, 'userprofile/view_dashboard_job.html', {'job': job})


# @login_required
# def edit_userprofile(request, user_id):
#     user = get_object_or_404(User, pk=job_id, created_by=request.user)

#     if request.method == 'POST':
#         form = AddJobForm(request.POST, instance=User)

#         if form.is_valid():
#             job = form.save(commit=False)
#             job.status = request.POST.get('status')
#             job.save()

#             return redirect('dashboard')
#     else:
#         form = AddJobForm(instance=job)
    
#     return render(request, 'job/edit_job.html', {'form': form, 'job': job})

def search_for_seeker(request):
    userprofile = User.objects.all()

    return render(request, 'userprofile/list_seekers.html',
                            {'userprofile': userprofile})
