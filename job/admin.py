from django.contrib import admin

from .models import Job, Application, Category

# Register your models here.
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Category)