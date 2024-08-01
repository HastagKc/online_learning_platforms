from django.urls import path
from .views import *

urlpatterns = [
    path('show_quiz/<int:course_id>', show_quiz, name='show_quiz')
]
