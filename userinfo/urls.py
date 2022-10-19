from django.urls import path, include
from .views import *
urlpatterns = [
    path('dashboard', AdminDashboard.as_view(), name='dashboard'),
]