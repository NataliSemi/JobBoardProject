from django.urls import path
from core.views import frontpage, signup
from django.contrib.auth import views

urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('signup/', signup, name="signup"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
]