from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='home-main'),
    path('my/<str:city>',  views.my_city, name='city'),
    path('myage/<int:age>',  views.my_age, name='age'),
    path('home', views.home, name='home'),
    path('students', views.student_list, name='student_list'),
]