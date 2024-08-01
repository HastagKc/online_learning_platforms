from django.urls import path
from .views import *

urlpatterns = [
    path('show_quiz/<int:course_id>', show_quiz, name='show_quiz'),
    path('take_quiz/<int:quiz_id>', take_quiz, name='take_quiz'),
]
