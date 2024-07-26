from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def user_is_teacher(function):
    @login_required(login_url='/accounts/log_in/')
    def wrap(request, *args, **kwargs):
        if hasattr(request.user, 'teacherprofile'):
            return function(request, *args, **kwargs)
        else:
            # Redirect to the index page if the user is not a teacher
            return redirect('index')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_student(function):
    @login_required(login_url='/accounts/log_in/')
    def wrap(request, *args, **kwargs):
        if hasattr(request.user, 'student_profile'):
            return function(request, *args, **kwargs)
        else:
            # Redirect to the index page if the user is not a student
            return redirect('index')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
