from django.http import HttpResponse
from django.shortcuts import render

from main.models import Student


def index(request):
    return HttpResponse("Hello world")


def my_city(request, city):
    return HttpResponse(f'Your city is {city}')


def my_age(request, age):
    return HttpResponse(f'Your age is {age}')


def home(request):
    return render(request, 'index.html')


def student_list(request):
    students = Student.objects.all()
    first_data = students.last()

    context = {"students": students,
               "first_student": first_data}
    return render(request, 'student.html', context)
