from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from .models import Quiz, Question, Option
from .forms import QuestionForm, OptionFormSet, AnswerForm, QuizForm
from online_learning_app.models import Course
# quiz


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


def update_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect('course_details', id=quiz.course.id)

    else:
        form = QuizForm(instance=quiz)

    context = {
        'form': form,
    }
    return render(request, 'quiz/create_quiz.html', context=context)


def detele_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
# questions


def create_question(request, quiz_id):
    # Fetching data
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz).prefetch_related('options')

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

            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
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
        'questions': questions,
    }

    return render(request, 'quiz/create_question.html', context)


# update


def update_question(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        # Process form data
        question_form = QuestionForm(request.POST, instance=question)
        option_formset = OptionFormSet(
            request.POST, queryset=Option.objects.filter(question=question))
        answer_form = AnswerForm(
            request.POST, instance=question.correct_answer if question.correct_answer else None)

        if question_form.is_valid() and option_formset.is_valid() and answer_form.is_valid():
            # Save the updated question
            question = question_form.save()

            # Save the updated options
            options = option_formset.save(commit=False)
            for option in options:
                option.question = question
                option.save()

            # Save the updated answer
            if answer_form.cleaned_data.get('answer_text'):
                answer = answer_form.save(commit=False)
                answer.question = question
                answer.save()

            # Redirect to a page that shows the updated quiz or question details
            # Adjust redirect as needed
            return redirect('create_question', quiz_id=quiz.id)

    else:
        # Initialize forms for GET request
        question_form = QuestionForm(instance=question)
        option_formset = OptionFormSet(
            queryset=Option.objects.filter(question=question))
        answer_form = AnswerForm(
            instance=question.correct_answer if question.correct_answer else None)

    context = {
        'quiz': quiz,
        'question_form': question_form,
        'option_formset': option_formset,
        'answer_form': answer_form,
    }

    return render(request, 'quiz/update_question.html', context)


# delete


def delete_question(request, quiz_id, question_id):
    question = get_object_or_404(Question, id=question_id, quiz_id=quiz_id)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question.delete()
    return redirect('create_question', quiz_id=quiz.id)


# quiz student

def show_quiz(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizes = Quiz.objects.filter(course=course)
    context = {
        'course': course,
        'quizes': quizes,
    }
    return render(request, 'quiz/quiz_stu/show_quiz.html', context=context)


def show_quiz_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz).prefetch_related('options')

    # Organize options by their related questions
    question_with_options = []
    for question in questions:
        options = question.options.all()
        question_with_options.append({
            'question': question,
            'options': options,
        })

    context = {
        'quiz': quiz,
        'question_with_options': question_with_options,
    }
    return render(request, 'quiz/quiz_stu/show_quiz_questions.html', context=context)
