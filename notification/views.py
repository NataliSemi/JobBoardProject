from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Notification


@login_required
def notification(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.MESSAGE:
            return redirect('view_application', user_id=notification.created_by.id)
        elif notification.notification_type == Notification.MESSAGE:
            return redirect('view_application', user_id=notification.created_by.id)

