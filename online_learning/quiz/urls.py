from django.urls import path
from .views import *

app_name = 'quiz'

urlpatterns = [
    path('show_quiz/<int:course_id>/', show_quiz, name='show_quiz'),
    path('take_quiz/<int:quiz_id>/', take_quiz, name='take_quiz'),
    path('quiz/<int:quiz_id>/results/', quiz_results, name='quiz_results'),

    # add quiz
    path('add_quiz/<int:course_id>/', add_quiz, name='add_quiz'),
]
