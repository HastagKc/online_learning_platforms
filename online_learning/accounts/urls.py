from django.urls import path
from .views import *

urlpatterns = [
    path('', choices, name="choices"),
    path('log_in/', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out'),
    path('stu_reg/', student_registration, name="student_registration"),
    path('tec_reg/', teacher_registration, name="teacher_registration"),
]
