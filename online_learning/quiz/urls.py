from django.urls import path
from .views import *
urlpatterns = [

    path('show_quiz/',show_quiz,name='show_quiz')

]
