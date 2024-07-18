from django.shortcuts import render, redirect
from .forms import CourseForm, CategoryForm, VideoForm
from .models import Course, Category

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'online_learning_app/index.html')


@login_required(login_url='/accounts/log_in/')
def teacher_dashboard(request):
    all_course = Course.objects.all()
    context = {
        'all_course': all_course
    }
    return render(request, 'online_learning_app/dashboard/teacher_dashboard.html', context=context)


@login_required(login_url='/accounts/log_in/')
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
    return render(request, 'online_learning_app/course/add_category.html', context=context)


@login_required(login_url='/accounts/log_in/')
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

    return render(request, 'online_learning_app/course/add_course.html', context=context)


@login_required(login_url='/accounts/log_in/')
def course_detail(request):
    '''
    this view will responsible to addtional information and content management about 
    course
    '''
    return render(request, 'online_learning_app/course/course_details.html')


@login_required
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            # Replace with your success URL
            return redirect('some_success_url')
    else:
        form = VideoForm(user=request.user)
    return render(request, 'online_learning_app/video/add_video.html', {'form': form})
