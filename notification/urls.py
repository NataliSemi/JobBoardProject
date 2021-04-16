from django.urls import path, include

from .views import notification

urlpatterns = [
    path('', notification, name='notifications'),
]