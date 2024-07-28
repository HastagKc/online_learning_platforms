from .models import Quiz, StudentProgress
from django.utils import timezone
from .models import Quiz, Question, Options, StudentProgress
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz
from django.shortcuts import render, get_object_or_404
from online_learning_app.models import Course
from .models import *

# Create your views here.

# quiz


def showQuiz(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizes = course.quizzes.all()
    context = {
        'quizes': quizes,
    }

    return render(request, 'quiz/quiz.html', context=context)


@login_required(login_url='/accounts/log_in/')
def takeQuiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.id}')
            if selected_option_id:
                selected_option = get_object_or_404(
                    Options, id=selected_option_id
                )
                is_correct = selected_option.question.answers.filter(
                    question=question, answer_text=selected_option
                ).exists()

                StudentProgress.objects.create(
                    student=request.user,
                    quiz=quiz,
                    question=question,
                    selected_option=selected_option,
                    is_correct=is_correct,
                    attempted_at=timezone.now()
                )

        # Calculate score
        total_questions = questions.count()
        correct_answers = StudentProgress.objects.filter(
            student=request.user, quiz=quiz, is_correct=True).count()
        score = (correct_answers / total_questions) * 100

        return redirect('quiz_results', quiz_id=quiz.id, score=int(score))

    question_options = [
        (question, question.options.all())
        for question in questions
    ]

    context = {
        'quiz': quiz,
        'questions': questions,
        'question_options': question_options,
    }

    return render(request, 'quiz/take_quiz.html', context)


def quiz_results(request, quiz_id, score):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    context = {
        'quiz': quiz,
        'score': score,
    }
    return render(request, 'quiz/quiz_results.html', context)
