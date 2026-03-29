from django.urls import path
import lesson.views as lesson_views

urlpatterns = [
    path("courses/", lesson_views.courses_list, name="courses_list"),
    path("teachers/", lesson_views.teachers_list, name="teachers_list"),
    path("classes/", lesson_views.classes_list, name="classes_list"),
    path("students/", lesson_views.students_list, name="students_list"),
    path("schedule/", lesson_views.schedule_list, name="schedule_list"),
]
