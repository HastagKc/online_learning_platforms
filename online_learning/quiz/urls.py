from django.urls import path
from .views import *

urlpatterns = [
    path('showQuiz/', showQuiz, name='showQuiz'),

]
