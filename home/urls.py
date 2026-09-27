from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('notes/', views.notes, name='notes'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('practice/', views.practice, name='practice'),
    path('ai-doubt/', views.ai_doubt, name='ai_doubt'),
    path('certificate/', views.certificate_demo, name='certificate_demo'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
      path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
]


