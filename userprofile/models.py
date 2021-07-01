from django.contrib.auth.models import User
from django.db import models

from job.models import Application

class StatusManager(models.Manager):
    def get_queryset(self):
        return super(StatusManager,
                     self).get_queryset().filter(is_employer=False)

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    about = models.CharField(max_length=200)
    is_employer = models.BooleanField(default=False)
    status = StatusManager() # Our custom manager

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])


class ConversationMessage(models.Model):
    application = models.ForeignKey(Application, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField()

    created_by = models.ForeignKey(User, related_name='conversationmessages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
