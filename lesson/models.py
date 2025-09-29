from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    courses = models.ManyToManyField(Courses, related_name='teachers')

    def __str__(self):
        return self.full_name

class Class(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.full_name

class Schedule(models.Model):
    subject = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class,on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)

    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.student_class} - {self.subject} ({self.day_of_week} {self.start_time})"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Courses,on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.value}"

