from django.shortcuts import render, redirect
from .models import CustomUserModel

import re

# Create your views here.


def is_complex_password(password):
    '''
    This function is check complexity of the password enter by user
    '''
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    regex = re.compile(pattern)
    if regex.match(password):
        return True
    else:
        return False


def validate_registration(username, email, password, con_password):
    '''
    This function if use to validate register input value
    '''
    try:
        if password != con_password:
            print("Passwords do not match.")
            return False

        if not is_complex_password(con_password):
            print("Password must be at least 8 characters and include uppercase, lowercase, digit, and special character.")
            return False

        if CustomUserModel.objects.filter(username=username).exists():
            print("Username already exists.")
            return False

        if CustomUserModel.objects.filter(email=email).exists():
            print("Email already exists.")
            return False

    except Exception as e:
        print(f"Error: {str(e)}")


def choices(request):
    '''

    This choices view will get one choices for registration
    either for student or for instructor

    '''
    if request.method == 'POST':
        if 'teacher' in request.POST:
            request.session['user_type'] = 'teacher'
            return redirect('teacher_registration')

        elif 'student' in request.POST:
            request.session['user_type'] = 'student'
            return redirect('student_registration')

        else:
            return redirect('choices')

    return render(request, 'accounts/choices.html')


def student_registration(request):
    '''
        This view is responsible for registering student
    '''

    return render(request, 'accounts/student_registration.html')


def teacher_registration(request):
    user_type = request.session.get('user_type')
    print(user_type, type(user_type))

    if user_type == 'teacher':
        is_teacher = True
    else:
        is_teacher = False

    if request.method == 'POST':
        data = request.POST
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        email = data['email']
        selected_gender = request.POST.get('gender', None)
        password = data['password']
        con_password = data['con_password']

        is_valid = validate_registration(
            username=username, email=email, con_password=con_password, password=password
        )
        if is_valid:
            # Create user if all checks pass
            user = CustomUserModel.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=username,
                email=email,
                gender=selected_gender,
                password=con_password,
                is_teacher=is_teacher,
            )
            print("User created successfully.")

    return render(request, 'accounts/teacher_registration.html', {'user_type': user_type})
