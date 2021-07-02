from django.urls import path
from . import views
from .api import api_search



urlpatterns = [
    path('api/search/', api_search, name='api_search'),
    # path('search/', views.search_job, name='search_job'),
    path('add/', views.add_job, name='add_job'),
    
    path('<int:id>/<slug:slug>/', views.job_detail, name='job_detail'),

    path('<slug:slug>/edit/', views.edit_job, name='edit_job'),
    path('<int:job_id>/apply_for_job/', views.apply_for_job, name='apply_for_job'),
]