from .models import Notification

def create_notification(request, to_user, notification_type, extra_id=0):
    notification = Notification.objects.create(to_user=to_user)