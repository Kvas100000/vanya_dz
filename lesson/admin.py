from django.contrib import admin
from .models import Courses, Teacher, Class, Student

admin.site.register(Courses)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)