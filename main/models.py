from django.db import models

LEVEL = (
    (1, "level 1"),
    (2, "level 2"),
    (3, "level 3"),
    (4, "level 4")
)

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


class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Xizmat turi'
        verbose_name_plural = 'Xizmat turlari'

    def __str__(self):
        return f'{self.name} {self.pk}'


class Menu(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Menyu'
        verbose_name_plural = 'Menyular'

    def __str__(self):
        return f'{self.name} {self.pk}'