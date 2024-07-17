from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('tech_dashboard/', teacher_dashboard, name="tech_dashboard"),
    path('course_details/', add_content, name='course_details'),
    path('add_course/', add_course, name='add_course'),
    path('add_category/', add_category, name='add_category'),
]
