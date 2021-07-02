from django.urls import path
from core.views import frontpage
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from userprofile.forms import (UserLoginForm)

urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('tag/<slug:tag_slug>/', frontpage, name='job_list_by_tag'),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',
                                                form_class=UserLoginForm), name='login'),
    # path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
]