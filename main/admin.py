from django.contrib import admin

# Register your models here.
from main.models import Student, MainGroup, Service, Menu


class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'level', 'group')
    list_filter = ('level',)


admin.site.register(Student, StudentAdmin)
admin.site.register(MainGroup)
admin.site.register(Service)
admin.site.register(Menu)
