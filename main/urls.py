from django.urls import path
from django.views.generic import TemplateView

from main import views
from main.views import ServiceList, ServiceDetailView

urlpatterns = [
    path('', views.index, name='home-main'),
    path('my/<str:city>',  views.my_city, name='city'),
    path('myage/<int:age>',  views.my_age, name='age'),
    path('home', views.home, name='home'),
    path('students', views.student_list, name='student_list'),
    # path('services', TemplateView.as_view(template_name="service.html"), name='service_list')
    path('services', ServiceList.as_view(), name='service_list'),
    path('services/<int:pk>', ServiceDetailView.as_view(), name='service_detail')
]