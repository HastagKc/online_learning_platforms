from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("Welcome to Online learning Platfroms")
    return render(request, 'online_learning_app/index.html')
