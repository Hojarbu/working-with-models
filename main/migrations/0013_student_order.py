# Generated by Django 3.1.2 on 2020-10-26 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201026_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
