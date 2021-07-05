from django.contrib.auth.decorators  import login_required
from django.shortcuts import render, redirect
from job.models import Application, Job
from django.shortcuts import get_object_or_404
from job.models import ConversationMessage
from notification.utilities import create_notification
from .models import User

from .forms import UserRegistrationForm, UserEditForm
 

@login_required
def dashboard(request):
    employed = Job.employed.all()
    archived = Job.archived.all()
    return render(request, 'userprofile/dashboard.html', 
                                                    {'employed': employed,
                                                    'archived':archived})


@login_required
def view_application(request, application_id):
    if request.user.is_employer:
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

    return render(request, 'userprofile/view_dashboard_job.html', 
                                                        {'job': job,
                                                        })



def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            #Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.is_active = True
            # Save the User object
            new_user.save()
            return render(request,
                    'register_done.html',
                    {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'userprofile/signup.html', {'user_form': user_form})



def seekers_list(request):
    users = User.objects.all()
    return render(request, 'userprofile/list_seekers.html', {'users': users})


def user_detail(request, user_id):
    user = get_object_or_404(User,pk=user_id)

    return render(request, 'userprofile/user_detail.html', {'user': user})


@login_required
def user_edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()

            return redirect('dashboard')
    else:
        user_form = UserEditForm(instance=user)
    
    return render(request, 'userprofile/edit_user.html', {'user_form': user_form, 'user': user})