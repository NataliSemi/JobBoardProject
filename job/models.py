from django.db import models
from userprofile.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from django.utils import timezone

from autoslug import AutoSlugField


class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique=True)

    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('job_list_by_category',
                       args=[self.slug])


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='active')

class EmployedManager(models.Manager):
    def get_queryset(self):
        return super(EmployedManager,
                     self).get_queryset().filter(status='employed')

class ArchivedManager(models.Manager):
    def get_queryset(self):
        return super(ArchivedManager,
                     self).get_queryset().filter(status='archived')


class Job(models.Model):

    ACTIVE = 'active'
    EMPLOYED = 'employed'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (EMPLOYED, 'Employed'),
        (ARCHIVED, 'Archived')
    )

    categories = models.ForeignKey(Category, related_name='job_category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    short_description = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    long_description = models.TextField(blank=True, null=True)

    company_name = models.CharField(max_length=255)
    company_place = models.CharField(max_length=255, blank=True, null=True)
    company_country = models.CharField(max_length=255, blank=True, null=True)

    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=ACTIVE)

    published = PublishedManager() # Our custom manager
    employed = EmployedManager()
    archived = ArchivedManager()

    tags = TaggableManager()

    class Meta:
        ordering = ('-created_at',)    
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title



class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()

    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ConversationMessage(models.Model):
    application = models.ForeignKey(Application, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField()

    created_by = models.ForeignKey(User, related_name='conversationmessages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']