from django.contrib import admin

# Register your models here.
from main.models import Student, MainGroup

admin.site.register(Student)
admin.site.register(MainGroup)
