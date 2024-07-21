from django.urls import path
from .views import *

urlpatterns = [
    # teacher dashboard
    path('dashboard/', dashboard, name="dashboard"),
    path('notifications/', notifications, name="notifications"),
    path('profile/', profile, name="profile"),
    path('courses_dashboard/', courses_dashboard, name="courses_dashboard"),

    # student dashboard

]
