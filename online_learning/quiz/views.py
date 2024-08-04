from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Options, Answer, UserQuizProgress, UserAnswer
from django.contrib.auth.decorators import login_required

from online_learning_app.models import Course

# Display quizzes related to a specific course


def show_quiz(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizes = course.quiz.all()
    context = {
        'course': course,
        'quizes': quizes
    }
    return render(request, 'quiz/show_quiz.html', context=context)

# Handle quiz-taking and scoring logic


@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    total_correct_in_attempt = 0  # Tracks correct answers in the current attempt

    if request.method == 'POST':
        # Get or create the user's quiz progress
        user_progress, created = UserQuizProgress.objects.get_or_create(
            user=request.user, quiz=quiz, defaults={
                'score': 0, 'completed': False}
        )

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

                # Check if the user has already answered this question
                user_answer, created = UserAnswer.objects.get_or_create(
                    user=request.user, question=question,
                    defaults={'answer': selected_option,
                              'is_correct': is_correct}
                )

                if not created:
                    # If the answer exists and was incorrect, update it if now correct
                    if not user_answer.is_correct and is_correct:
                        user_answer.is_correct = True
                        user_answer.answer = selected_option
                        user_answer.save()
                        total_correct_in_attempt += 1
                else:
                    # If the answer is newly created and correct, increment the score
                    if is_correct:
                        total_correct_in_attempt += 1

        # Update the user's total score if there were new correct answers
        if total_correct_in_attempt > 0:
            user_progress.score += total_correct_in_attempt
            user_progress.save()

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
