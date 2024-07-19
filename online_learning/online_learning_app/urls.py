from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),

    # teacher dashboard
    path('tech_dashboard/', teacher_dashboard, name="tech_dashboard"),

    # category
    path('add_category/', add_category, name='add_category'),
    path('update_category/<int:id>/', update_category, name='update_category'),
    path('delete_category/<int:id>/', delete_category, name='delete_category'),

    # course
    path('course_details/<int:id>/', course_detail, name='course_details'),
    path('add_course/', add_course, name='add_course'),

    # video
    path('add_video/', add_video, name='add_video')
]
