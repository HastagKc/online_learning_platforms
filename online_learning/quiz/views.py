from django.shortcuts import render,get_list_or_404

# Create your views here.

# quiz


def showQuiz(request):
    return render(request, 'online_learning_app/quiz/quiz.html')



