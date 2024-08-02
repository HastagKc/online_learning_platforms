
from django.shortcuts import render, get_object_or_404, redirect

from online_learning_app.models import Course
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.


def show_quiz(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizes = course.quiz.all()
    context = {
        'course': course,
        'quizes': quizes
    }
    return render(request, 'quiz/show_quiz.html', context=context)


@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    score = 0

    if request.method == 'POST':
        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.id}')
            if selected_option_id:
                selected_option = get_object_or_404(
                    Options, id=selected_option_id)

                # Find the correct answer for the question
                correct_answer = Answer.objects.filter(
                    question=question).first()

                is_correct = (selected_option.option_text ==
                              correct_answer.answer) if correct_answer else False
                if is_correct:
                    score += 1

                UserAnswer.objects.create(
                    user=request.user,
                    question=question,
                    answer=selected_option,
                    is_correct=is_correct
                )

        UserQuizProgress.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            completed=True
        )
        return redirect('quiz_results', quiz_id=quiz.id)

    context = {
        'questions': questions,
    }
    return render(request, 'quiz/take_quiz.html', context)


@login_required
def quiz_results(request, quiz_id):
    progress = get_object_or_404(
        UserQuizProgress, quiz_id=quiz_id, user=request.user)

    context = {
        'progress': progress,
    }
    return render(request, 'quiz/quiz_results.html', context)
