from django.contrib import admin

# Register your models here.
from main.models import Student, MainGroup, Service

admin.site.register(Student)
admin.site.register(MainGroup)
admin.site.register(Service)
