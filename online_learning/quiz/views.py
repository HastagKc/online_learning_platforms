from .models import Question
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .models import Quiz, Question, Option, Answer
from .models import Quiz, Question
from .forms import QuestionForm, OptionFormSet, AnswerForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, OptionFormSet, AnswerForm, QuizForm
from .models import Quiz, Question, Course, Option, Answer


def create_quiz(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.course = course
            quiz.save()
            return redirect('course_details', id=course_id)
    else:
        form = QuizForm()

    context = {
        'form': form,
        'course': course,
    }
    return render(request, 'quiz/create_quiz.html', context=context)


def create_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        option_formset = OptionFormSet(request.POST)
        answer_form = AnswerForm(request.POST)

        if question_form.is_valid() and option_formset.is_valid() and answer_form.is_valid():
            question = question_form.save(commit=False)
            question.quiz = quiz
            question.save()

            options = option_formset.save(commit=False)
            for option in options:
                option.question = question
                option.save()

            answer = answer_form.save(commit=False)
            answer.question = question
            answer.save()

            # Redirect to the quiz detail page after question creation
            return redirect('home')
        else:
            print(question_form.errors)
            print(option_formset.errors)
            print(answer_form.errors)

    else:
        question_form = QuestionForm()
        option_formset = OptionFormSet(queryset=Option.objects.none())
        answer_form = AnswerForm()

    context = {
        'quiz': quiz,
        'question_form': question_form,
        'option_formset': option_formset,
        'answer_form': answer_form,
    }

    return render(request, 'quiz/create_question.html', context)


# update


def update_question(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = get_object_or_404(Question, id=question_id)

    # Initialize forms with the existing question data
    question_form = QuestionForm(instance=question)
    option_formset = OptionFormSet(
        queryset=Option.objects.filter(question=question))
    answer_form = AnswerForm(instance=question.correct_answer)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST, instance=question)
        option_formset = OptionFormSet(request.POST, instance=question)
        answer_form = AnswerForm(
            request.POST, instance=question.correct_answer)

        if question_form.is_valid() and option_formset.is_valid() and answer_form.is_valid():
            # Save the updated question
            question = question_form.save()

            # Save the updated options
            options = option_formset.save(commit=False)
            for option in options:
                option.question = question
                option.save()

            # Save the updated answer
            if answer_form.cleaned_data['answer_text']:
                answer = answer_form.save(commit=False)
                answer.question = question
                answer.save()

            # Redirect to the quiz detail page or another page after updating the question
            return redirect('home')  # Update with the appropriate redirect URL

    context = {
        'quiz': quiz,
        'question_form': question_form,
        'option_formset': option_formset,
        'answer_form': answer_form,
    }

    return render(request, 'quiz/create_or_update_question.html', context)


# delete


def delete_question(request, quiz_id, question_id):
    question = get_object_or_404(Question, id=question_id, quiz_id=quiz_id)

    if request.method == 'POST':
        # Delete the question
        question.delete()
        # Show a success message
        messages.success(request, 'Question deleted successfully.')
        # Redirect to the quiz detail page or another relevant page
        return redirect('home')  # Update with the appropriate redirect URL

    # Render a confirmation template (optional)
    return render(request, 'quiz/confirm_delete.html', {'question': question})
