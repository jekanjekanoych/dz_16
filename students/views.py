from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# from django.urls import reverse

from students.forms import StudentForm
from students.models import Student


def index(request):
    return HttpResponse("Student does not exist")


def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/students/")
    else:
        s = Student.objects.last()
        form = StudentForm(instance=s)
        return render(request, "student.html", {"form": form})


def students(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})
