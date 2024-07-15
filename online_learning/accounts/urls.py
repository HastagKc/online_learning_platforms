from django.urls import path
from .views import choices, student_registration, teacher_registration

urlpatterns = [
    path('', choices, name="choices"),
    path('stu_reg/', student_registration, name="student_registration"),
    path('tec_reg/', teacher_registration, name="teacher_registration"),
]
