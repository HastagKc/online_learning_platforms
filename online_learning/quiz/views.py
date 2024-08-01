from django.shortcuts import render, get_object_or_404

from online_learning_app.models import Course

# Create your views here.


def show_quiz(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizes = course.quiz.all()
    context = {
        'course': course,
        'quizes': quizes
    }
    return render(request, 'quiz/show_quiz.html', context=context)
