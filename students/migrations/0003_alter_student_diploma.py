# Generated by Django 4.2.2 on 2023-06-26 19:10

from django.db import migrations, models
import students.models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0002_student_diploma"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="diploma",
            field=models.ImageField(
                null=True, upload_to=students.models.upload_diploma
            ),
        ),
    ]
