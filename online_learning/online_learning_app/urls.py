from django.urls import path
from .views import *
urlpatterns = [
    # online learning main route
    path('', home, name="home"),
    path('details_page/<int:id>/', details_page, name='details_page'),

    # teacher dashboard
    path('tech_dashboard/', teacher_dashboard, name="tech_dashboard"),

    # category
    path('add_category/', add_category, name='add_category'),
    path('update_category/<int:id>/', update_category, name='update_category'),
    path('delete_category/<int:id>/', delete_category, name='delete_category'),

    # course
    path('course_details/<int:id>/', course_detail, name='course_details'),
    path('add_course/', add_course, name='add_course'),
    path('update_course/<int:id>/', update_course, name='update_course'),
    path('delete_course/<int:id>/', delete_course, name='delete_course'),

    # video
    path('add_video/', add_video, name='add_video'),
    path('update_video/<int:id>/', update_video, name='update_video'),
    path('delete_video/<int:id>/', delete_video, name='delete_video'),


    # study pannel
    path('study_pannel/<int:id>/', study_pannel, name='study_pannel'),
    path('watch_video/<int:id>/', watch_video, name='watch_video'),



    # test
    path('dashboardTest/', dashboardTest, name='dashboardTest')

]
