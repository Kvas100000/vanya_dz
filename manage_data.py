import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vanya_dz.settings')
django.setup()

from lesson.models import Courses, Teacher, Class, Student, Schedule, Grade


def add_subject():
    name = input("Назва предмета: ").strip()
    if Courses.objects.filter(name=name).exists():
        print("Такой предмет уже существует")
    else:
        Courses.objects.create(name=name)
        print("Предмет добавлен")

def add_teacher():
    full_name = input("ПІБ Учителя: ").strip()
    course_name = input("Название предмета: ").strip()
    course = Courses.objects.filter(name=course_name).first()
    if not course:
        print("Предмета не найден")
        return
    teacher, created = Teacher.objects.get_or_create(full_name=full_name)
    teacher.courses.add(course)

    if created:
        print("Учителя и предмет добавлен")
    else:
        print("Учитель уже есть предмет добавлен")


def add_class():
    name = input("Название класса: ").strip()
    if Class.objects.filter (name=name).exists():
        print("Такой класс уже есть")
    else:
        Class.objects.create(name=name)
        print("Класс добавлен")

def add_student():
    full_name = input("ПІБ ученика: ").strip()
    class_name = input("Класс: ").strip()
    student_class = Class.objects.filter(name=class_name).first()
    if not student_class:
        print("Класс не найден")
        return
    Student.objects.create(full_name=full_name, student_class=student_class)
    print("Добавлено ученика")


def add_schedule():
    day = input("День недели: ").strip()
    start = input("Начало(HH:MM): ").strip()
    end = input("Конец(HH:MM): ").strip()
    subject_name = input("Предмет: ").strip()
    class_name = input("Класс: ").strip()
    teacher_name = input("Учитель: ").strip()

    subject = Courses.objects.filter(name=subject_name).first()
    student_class = Class.objects.filter(name=class_name).first()
    teacher = Teacher.objects.filter(full_name=teacher_name).first()

    if not subject or not student_class or not teacher:
        print("Один из обьектов не обнаружен ")
        return

    Schedule.objects.create(
        subject=subject,
        teacher=teacher,
        student_class=student_class,
        day_of_week=day,
        start_time=start,
        end_time=end
    )
    print("Занятие добавлено в расписание.")

def add_grade():
    student_name = input("ФИО ученика: ").strip()
    subject_name = input("Предмет: ").strip()
    value = input("Оценка (1–12): ").strip()

    student = Student.objects.filter(full_name=student_name).first()
    subject = Courses.objects.filter(name=subject_name).first()

    if not student or not subject:
        print("Ученик или предмет не обнаружен")
        return

    Grade.objects.create(student=student, subject=subject, value=int(value))
    print("Оценка добавлена")

def check_subjects():
    subjects = Courses.objects.all()
    if not subjects:
        print("Предметов не добавлено")
    else:
        print("Список предметов:")
        for subject in subjects:
            print(f"- {subject.name}")

def check_teachers():
    teachers = Teacher.objects.all()
    if not teachers:
        print("Учителей не добавлено")
    else:
        print("Список учителей:")
        for teacher in teachers:
            print(f"- {teacher.full_name}")

def check_classes():
    classes = Class.objects.all()
    if not classes:
        print("Классы не созданы")
        return

    for student_class in classes:
        print(f"\n Класс: {student_class.name}")
        students = student_class.students.all()
        if students:
            for student in students:
                print(f" {student.full_name}")
        else:
            print("Нету учеников")

def check_schedule():
    day = input("Введите день недели ").strip()
    lessons = Schedule.objects.filter(day_of_week=day).order_by('start_time')

    if not lessons:
        print(f"Нет занятий на {day}.")
        return

    print(f"\nРасписание на {day}:")
    for lesson in lessons:
        print(f"- {lesson.start_time.strftime('%H:%M')}–{lesson.end_time.strftime('%H:%M')} | "
              f"{lesson.student_class.name} | {lesson.subject.name} | {lesson.teacher.full_name}")

def check_grades():
    full_name = input("Введіть ПІБ учня: ").strip()
    student = Student.objects.filter(full_name=full_name).first()

    if not student:
        print("Ученика не найдено")
        return

    grades = Grade.objects.filter(student=student)

    if not grades:
        print("У ученика нет оценок")
        return

    print(f"\n Оценки {student.full_name}:")
    for grade in grades:
        print(f"- {grade.subject.name}: {grade.value}")

def main():
    actions = {
        "1": ("Додати предмет", add_subject),
        "2": ("Додати вчителя", add_teacher),
        "3": ("Додати клас", add_class),
        "4": ("Додати учня", add_student),
        "5": ("Додати заняття в розклад", add_schedule),
        "6": ("Додати оцінку", add_grade),
        "7": ("Показати всі предмети", check_subjects),
        "8": ("Показати класи з учнями", check_classes),
        "9": ("Показати розклад на день", check_schedule),
        "10": ("Показати оцінки учня", check_grades),
        "11": ("Показати вчителів", check_teachers),
        "0": ("Вихід", None),
    }

    while True:
        print("\nМеню:")
        for key, (label, _) in actions.items():
            print(f"{key} - {label}")

        choice = input("Ваш вибір: ").strip()
        action = actions.get(choice)

        if not action:
            print("Невірний вибір.")
        elif choice == "0":
            print("До зустрічі!")
            break
        else:
            action[1]()
if __name__ == "__main__":
    main()


