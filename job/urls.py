from django.urls import path
from . import views

urlpatterns = [
    path('jobs/<int:job_id>/', views.job_detail, name="job_detail"),
    path('jobs/add/', views.add_job, name="add_job"),
]