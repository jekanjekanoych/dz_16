from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from students.forms import StudentForm
from students.models import Student


def index(request):
    return HttpResponse("Student does not exist")


def student(request):
    form = StudentForm(request.POST, request.FILES)
    if request.method == "GET":
        return render(request, "student.html", {"form": form})

    if form.is_valid():
        form.save()

        return redirect(reverse(students))
    return render(request, "student.html", {"form": form})


def students(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})
