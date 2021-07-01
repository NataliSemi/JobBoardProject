from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/seekers', views.search_for_seeker, name="seekers_list"),
    path('job/<int:job_id>/', views.view_dashboard_job, name='view_dashboard_job'),
    path('application/<int:application_id>/', views.view_application, name='view_application'),

]