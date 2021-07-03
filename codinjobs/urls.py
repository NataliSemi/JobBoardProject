from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('yoasdfdsak34seursa9876ca/', admin.site.urls),
    path('', include('core.urls')),
    path('jobs/', include('job.urls')),
    path('', include('userprofile.urls')),
    path('notifications/', include('notification.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)