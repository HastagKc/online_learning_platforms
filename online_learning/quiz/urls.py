from django.urls import path
from .views import *

urlpatterns = [
    # quiz
    path('create_quiz/<int:course_id>/', create_quiz, name='create_quiz'),
    path('update_quiz/<int:quiz_id>/', update_quiz, name='update_quiz'),
    path('detele_quiz/<int:quiz_id>/', detele_quiz, name='detele_quiz'),

    # question
    path('create_question/<int:quiz_id>/',
         create_question, name='create_question'),
    path('update_question/<int:quiz_id>/<int:question_id>/',
         update_question, name='update_question'),


    path('delete_question/<int:quiz_id>/<int:question_id>/',
         delete_question, name='delete_question'),


]
