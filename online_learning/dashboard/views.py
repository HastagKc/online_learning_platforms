from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from online_learning_app.models import Course, Category

# Create your views here.

# dashboard


@login_required(login_url='/accounts/log_in/')
def dashboard(request):
    return render(request, 'dashboard/teacher/dashboard.html')

# notifications


@login_required(login_url='/accounts/log_in/')
def notifications(request):
    return render(request, 'dashboard/teacher/notifications.html')


# profile
@login_required(login_url='/accounts/log_in/')
def profile(request):
    return render(request, 'dashboard/teacher/profile.html')


# tables
@login_required(login_url='dashboard/accounts/log_in/')
def courses_dashboard(request):
    courses = Course.objects.all()
    category = Category.objects.all()
    context = {
        'courses': courses,
        'category': category,
    }

    return render(request, 'dashboard/teacher/courses.html', context=context)
