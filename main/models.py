from django.db import models


# class TimeStamped(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True, verbos)
#
#     class Meta:
#         proxy = True
from pip._vendor.requests import Response


class MainGroup(models.Model):
    name = models.CharField(max_length=128, verbose_name='Guruh nomi')
    description = models.TextField(blank=True, null=False, verbose_name='Ma\'lumot')

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'Guruh'
        verbose_name_plural = 'Guruhlar'


class Student(models.Model):
    LEVEL = (
        (1, "level 1"),
        (2, "level 2"),
        (3, "level 3"),
        (4, "level 4")
    )

    full_name = models.CharField(max_length=50)
    group = models.ForeignKey(MainGroup, on_delete=models.CASCADE, null=True)
    dob = models.DateField()
    photo = models.ImageField(upload_to='student/y/m/d', null=True)
    order = models.IntegerField(default=0)
    level = models.IntegerField(choices=LEVEL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'

    def __str__(self):
        return f'{self.full_name} {self.pk}'




# class ProxyStudent(CustomModel):
#
#     def get_full_name(self):
#         return self.full_name

