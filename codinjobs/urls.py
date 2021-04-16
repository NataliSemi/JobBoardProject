from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('jobs/', include('job.urls')),
    path('', include('userprofile.urls')),
    path('notifications/', include('notification.urls')),
]
