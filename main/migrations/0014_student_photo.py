# Generated by Django 3.1.2 on 2020-10-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_student_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to='student/y/m/d'),
        ),
    ]
