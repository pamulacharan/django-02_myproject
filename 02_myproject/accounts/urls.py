from django.urls import path
from . import views
from .views import register, login_success


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('login_success/', login_success, name='login_success'),
]
