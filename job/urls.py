from django.urls import path
from . import views

urlpatterns = [
    path('jobs/<int:job_id>/', views.job_detail, name="job_detail"),
]