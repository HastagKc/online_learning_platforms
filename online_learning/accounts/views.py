from django.shortcuts import render, redirect

# Create your views here.


def choices(request):
    '''

    This choices view will get one choices for registration 
    either for student or for instructor

    '''
    if request.method == 'POST':
        if 'teacher' in request.POST:
            return redirect('teacher_registration')
        elif 'student' in request.POST:
            return redirect('student_registration')

        else:
            return redirect('choices')

    return render(request, 'accounts/choices.html')


def student_registration(requets):
    return render(requets, 'accounts/student_registration.html')


def teacher_registration(requets):
    return render(requets, 'accounts/teacher_registration.html')
