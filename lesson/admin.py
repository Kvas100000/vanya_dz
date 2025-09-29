from django.contrib import admin
from .models import Courses, Teacher, Class, Student,Grade, Schedule

admin.site.register(Courses)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Schedule)