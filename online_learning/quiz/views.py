from django.shortcuts import render
from .forms import *

# Create your views here.


def show_quiz(request):
    form = OptionForm

    context = {
        'form': form
    }
    return render(request, 'quiz/show_quiz.html', context=context)
