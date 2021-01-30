from django.urls import path
from . import views
#Password reset functionality
form django.contrib.auth import views as  auth_views



urlpatterns = [
    path('profile/',views.profile, name='profile'),
    path('registration/',views.registration, name='registration'),
    
]