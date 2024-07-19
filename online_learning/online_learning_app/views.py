from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm, CategoryForm, VideoForm
from .models import Course, Category, Video

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'online_learning_app/index.html')

# ----------------------------- Teacher Dashboard --------------------------------------------


@login_required(login_url='/accounts/log_in/')
def teacher_dashboard(request):
    all_course = Course.objects.all()
    all_categories = Category.objects.all()
    context = {
        'all_course': all_course,
        'all_categories': all_categories,
    }
    return render(request, 'online_learning_app/dashboard/teacher_dashboard.html', context=context)


# ------------------------- Category ------------------------------------------
@login_required(login_url='/accounts/log_in/')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cate = form.save(commit=False)
            cate.created_by = request.user.username
            cate.save()
            return redirect('tech_dashboard')
    else:
        form = CategoryForm()

    context = {
        'cate_form': form,
    }
    return render(request, 'online_learning_app/category/add_category.html', context=context)


@login_required(login_url='/accounts/log_in/')
def update_category(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('tech_dashboard')

    else:
        form = CategoryForm(instance=category)

        context = {
            'cate_form': form,
        }
    return render(request, 'online_learning_app/category/add_category.html', context=context)


@login_required(login_url='/accounts/log_in/')
def delete_category(request, id):
    if request.method == 'POST':
        category = get_object_or_404(Category, pk=id)
        category.delete()
        return redirect('tech_dashboard')


def confirm_delete(request, id):
    pass

# ------------------------------------ Course -----------------------------------------------


@login_required(login_url='/accounts/log_in/')
def course_detail(request, id):
    '''
    this view will responsible to addtional information and content management about 
    course
    '''
    course = Course.objects.filter(id=id)
    course_videos = Video.objects.filter(course=id)

    context = {
        'course': course,
        'course_videos': course_videos,
    }
    return render(request, 'online_learning_app/course/course_details.html', context=context)


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


# ---------------------------------------- video -----------------------------------------------
@login_required
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            video = form.save()
            return redirect('tech_dashboard')
    else:
        form = VideoForm(user=request.user)
    return render(request, 'online_learning_app/video/add_video.html', {'form': form})
