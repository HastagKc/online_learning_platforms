from django.shortcuts import render, redirect
from .forms import CourseForm, CategoryForm

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'online_learning_app/index.html')


def teacher_dashboard(request):
    return render(request, 'online_learning_app/teacher_dashboard.html')


@login_required(login_url='/accounts/login/')
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user.username
            course.save()
            return redirect('tech_dashboard')
    else:
        form = CourseForm()

    context = {
        'content_form': form,
    }

    return render(request, 'online_learning_app/add_course.html', context=context)


@login_required(login_url='/accounts/login/')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tech_dashboard')
    else:
        form = CategoryForm()

    context = {
        'cate_form': form,
    }
    return render(request, 'online_learning_app/add_category.html', context=context)


def add_content(request):
    return render(request, 'online_learning_app/course_details.html')


def add_video(request):
    return render(request, 'online_learning_app/course_details.html')
