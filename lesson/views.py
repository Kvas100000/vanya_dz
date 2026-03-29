from django.shortcuts import render
from lesson.models import Courses,Teacher,Class,Student,Schedule,Grade

def courses_list(request):
    courses = Courses.objects.all()
    return render(request,"lesson/courses_list.html",{"courses_list": courses,})

def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, "lesson/teachers_list.html", {"teachers": teachers})

def classes_list(request):
    classes = Class.objects.all()
    return render(request, "lesson/classes_list.html", {"classes": classes})

def students_list(request):
    students = Student.objects.all()
    return render(request, "lesson/students_list.html", {"students": students})

def schedule_list(request):
    schedule = Schedule.objects.all().order_by("day_of_week", "start_time")
    return render(request, "lesson/schedule_list.html", {"schedule": schedule})


