from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('tech_dashboard/', teacher_dashboard, name="tech_dashboard"),
    path('add_course/', add_course, name='add_course'),
    path('add_category/', add_category, name='add_category'),

    path('course_details/<int:id>/', course_detail, name='course_details'),
    path('add_video/', add_video, name='add_video')
]
