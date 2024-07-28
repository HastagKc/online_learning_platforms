from django.urls import path
from .views import *

urlpatterns = [
    path('showQuiz/<int:course_id>/', showQuiz, name='showQuiz'),
    path('takeQuiz/<int:quiz_id>/', takeQuiz, name='takeQuiz'),

    path('quiz_results/<int:quiz_id>/results/<int:score>/',
         quiz_results, name='quiz_results'),
]
