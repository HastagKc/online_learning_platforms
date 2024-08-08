from django.urls import path
from .views import *

urlpatterns = [
    path('create_quiz/<int:course_id>/', create_quiz, name='create_quiz'),
    path('create_question/<int:quiz_id>/',
         create_question, name='create_question'),


]
