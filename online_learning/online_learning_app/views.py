from .models import Course, Video
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm, CategoryForm, VideoForm, PDFForm
from .models import Course, Category, Video, PDF

from django.contrib.auth.decorators import login_required
# for redirect into same page
from django.http import HttpResponseRedirect
# --------------------------------- Online learning app --------------------------------------


def home(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    context = {
        'courses': courses,
        'categories': categories,
    }
    return render(request, 'online_learning_app/index.html', context=context)


@login_required(login_url='/accounts/log_in/')
def details_page(request, id):
    course = get_object_or_404(Course, id=id)
    context = {
        'course': course,
    }
    return render(request, 'online_learning_app/details_page.html', context=context)

# ----------------------------- Teacher Dashboard --------------------------------------------

# ------------------------- Category ------------------------------------------


@login_required(login_url='/accounts/log_in/')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cate = form.save(commit=False)
            cate.created_by = request.user.username
            cate.save()
            return redirect('courses_dashboard')
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
            return redirect('courses_dashboard')

    else:
        form = CategoryForm(instance=category)

        context = {
            'cate_form': form,
        }
    return render(request, 'online_learning_app/category/add_category.html', context=context)


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('courses_dashboard')


# ------------------------------------ Course -----------------------------------------------


@login_required(login_url='/accounts/log_in/')
def course_detail(request, id):
    '''
    this view will responsible to addtional information and content management about
    course
    '''
    course = Course.objects.filter(id=id)
    course_videos = Video.objects.filter(course=id)
    course_pdf = PDF.objects.filter(course=id)

    context = {
        'course': course,
        'course_videos': course_videos,
        'course_pdf': course_pdf,
    }
    return render(request, 'online_learning_app/course/course_details.html', context=context)


@login_required(login_url='/accounts/log_in/')
def add_course(request):
    '''
    this view add new course
    '''
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user.username
            course.save()
            return redirect('courses_dashboard')
    else:
        form = CourseForm()

    context = {
        'form': form,
    }

    return render(request, 'online_learning_app/course/add_course.html', context=context)


def update_course(request, id):
    '''
    This view update the content of the course
    '''
    course = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses_dashboard')

    else:
        form = CourseForm(instance=course)

    return render(request, 'online_learning_app/course/add_course.html', {'form': form})


def delete_course(request, id):
    course = get_object_or_404(Course, pk=id)
    course.delete()
    return redirect('courses_dashboard')

    # ---------------------------------------- video -----------------------------------------------


@login_required(login_url='/accounts/log_in/')
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            video = form.save()
            # Assuming the video model has a ForeignKey to the course model
            course_id = video.course.id
            return redirect('course_details', id=course_id)
    else:
        form = VideoForm(user=request.user)
    return render(request, 'online_learning_app/video/add_video.html', {'form': form})


@login_required(login_url='/accounts/log_in/')
def update_video(request, id):
    video = get_object_or_404(Video, pk=id)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            video = form.save()
            course_id = video.course.id
            return redirect('course_details', id=course_id)

    else:
        form = VideoForm(instance=video)

    return render(request, 'online_learning_app/video/add_video.html', {'form': form})


@login_required(login_url='/accounts/log_in/')
def delete_video(request, id):
    video = get_object_or_404(Video, pk=id)
    video.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# content access page

@login_required(login_url='/accounts/log_in/')
def study_pannel(request, id):
    course = get_object_or_404(Course, id=id)
    related_videos = course.videos.all()  # Accessing related videos
    # Handling case when there are no videos
    first_video = related_videos[0] if related_videos else None
    context = {
        'course': course,
        'related_videos': related_videos,
        'video': first_video,  # Use 'video' for consistency in template
    }
    return render(request, 'online_learning_app/study_pannel.html', context=context)


@login_required(login_url='/accounts/log_in/')
def watch_video(request, id):
    video = get_object_or_404(Video, id=id)
    course = video.course
    related_videos = course.videos.all()  # Accessing related videos
    context = {
        'course': course,
        'related_videos': related_videos,
        'video': video,  # Specific video to watch
    }
    return render(request, 'online_learning_app/study_pannel.html', context=context)


# ------------------------------  PDF --------------------------------------------------
@login_required(login_url='/accounts/log_in/')
def add_course_pdf(request):
    '''
    This view is responsible for adding course pdf to Pdf model
    '''
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PDFForm()
    return render(request, 'online_learning_app/pdf/add_course_pdf.html', {'form': form})


@login_required(login_url='/accounts/log_in/')
def update_course_pdf(request, id):
    '''
    this view is responsible to update upf file details
    '''
    pdf = get_object_or_404(PDF, id=id)
    if request.method == 'POST':
        form = PDFForm(request.POST, instance=pdf)
        if form.is_valid():
            pdf = form.save()
            course_id = pdf.course.id
            return redirect('course_details', id=course_id)

    else:
        form = PDFForm(instance=pdf)
    return render(request, 'online_learning_app/pdf/add_course_pdf.html', {'form': form})


@login_required(login_url='/accounts/log_in/')
def delete_course_pdf(request, id):
    '''
    this views is responsible for deleting courses pdf
    '''
    pdf = get_object_or_404(PDF, id=id)
    pdf.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
