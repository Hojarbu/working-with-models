from django.db import models


# class TimeStamped(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True, verbos)
#
#     class Meta:
#         proxy = True


class Student(models.Model):
    full_name = models.CharField(max_length=50)
    group_number = models.PositiveIntegerField()
    dob = models.DateField()
    level = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'

    def __str__(self):
        return f'{self.full_name} {self.pk}'


# class ProxyStudent(CustomModel):
#
#     def get_full_name(self):
#         return self.full_name

