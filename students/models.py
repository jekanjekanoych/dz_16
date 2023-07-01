import uuid

from django.db import models


def upload_diploma(instance, filename):
    return f"diploma/{uuid.uuid4()}/{filename}"


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    city = models.CharField(max_length=200)
    diploma = models.ImageField(upload_to=upload_diploma, null=True)

    def __str__(self):
        return "%s %s %i %s %i" % (
            self.first_name,
            self.last_name,
            self.age,
            self.city,
            self.id,
        )
