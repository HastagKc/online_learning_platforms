from django.urls import path
from .views import *

urlpatterns = [
    # teacher dashboard
    path('dashboard/', dashboard, name="dashboard"),
    path('notifications/', notifications, name="notifications"),
    path('courses_dashboard/', courses_dashboard, name="courses_dashboard"),

    path('profile/', teacher_profile, name="profile"),
    path('update_teacher_profile/<int:id>', update_teacher_profile,
         name='update_teacher_profile'),


    # student dashboard

]
