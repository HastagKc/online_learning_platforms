from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from online_learning_app.models import Course, Category
from .models import TeacherProfile
from accounts.models import CustomUserModel

# Create your views here.

# dashboard


@login_required(login_url='/accounts/log_in/')
def dashboard(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'dashboard/teacher/dashboard.html', context=context)

# notifications


@login_required(login_url='/accounts/log_in/')
def notifications(request):
    return render(request, 'dashboard/teacher/notifications.html')

# ------------------------------------ Profile -------------------------------------------------
# profile


@login_required(login_url='/accounts/log_in/')
def teacher_profile(request):
    return render(request, 'dashboard/teacher/profile.html')


# Update Teacher Profile


@login_required(login_url='/accounts/log_in/')
def update_teacher_profile(request, id):
    teacher = get_object_or_404(CustomUserModel, id=id)
    if request.method == 'POST':
        profile_img = request.FILES.get('profile_image')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        bio = request.POST.get('bio')

        errors = []

        # Validation
        if not phone_number.isdigit() or len(phone_number) < 10:
            errors.append(
                "Phone number must contain only digits and be at least 10 digits long")

        if not errors:
            try:
                # Get or create the teacher profile linked to the current user
                teacher_profile, created = TeacherProfile.objects.get_or_create(
                    user=request.user
                )
                # Update the profile with new data
                teacher_profile.profile_img = profile_img
                teacher_profile.age = age
                teacher_profile.address = address
                teacher_profile.phone_number = phone_number
                teacher_profile.bio = bio
                teacher_profile.save()
                return redirect('profile')
            except ValidationError as e:
                errors.append(str(e))
        else:
            for error in errors:
                print(error)

    context = {
        'teacher': teacher,
    }

    return render(request, 'dashboard/teacher/update_teacher_profile.html', context=context)

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
