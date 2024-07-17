from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('tech_dashboard', teacher_dashboard, name="tech_dashboard"),
]
