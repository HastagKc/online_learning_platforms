from django.urls import path
from .views import *

urlpatterns = [
    path('showQuiz/<int:course_id>/', showQuiz, name='showQuiz'),
    path('takeQuiz/<int:quiz_id>/', takeQuiz, name='takeQuiz'),

]
