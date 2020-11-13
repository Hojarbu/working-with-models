from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from main.models import Student, MainGroup, Service, Menu


def index(request):
    menu = Menu.objects.all()
    return HttpResponse("Hello world", {"menu":menu})


def my_city(request, city):
    return HttpResponse(f'Your city is {city}')


def my_age(request, age):
    return HttpResponse(f'Your age is {age}')


def home(request):
    return render(request, 'index.html')


def student_list(request):
    students = Student.objects.order_by('order').filter(level=1)
    # first_data = students.last()

    context = {"students": students

               }
    return render(request, 'student.html', context)


class ServiceList(ListView):
    model = Service
    template_name = "service.html"
    context_object_name = 'service_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['students'] = Student.objects.all()
        context['services'] = Service.objects.all()
        return context


class ServiceDetailView(DetailView):
    model = Service
    template_name = "service_detail.html"
