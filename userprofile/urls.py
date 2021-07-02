from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('seekers/', views.seekers_list, name="seekers"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    
    path('job/<int:job_id>/', views.view_dashboard_job, name='view_dashboard_job'),
    path('application/<int:application_id>/', views.view_application, name='view_application'),

]