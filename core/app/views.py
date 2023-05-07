# Create your views here.
from django.shortcuts import render , get_object_or_404
from .models import School, Teacher, Student, Class, Subject, Grade, Lesson

def error_404(request, exception):
    return render(request, 'pages/404.html', {})

def school_list(request):
    schools = School.objects.all()
    context = {
        'schools': schools,
    }
    return render(request, 'pages/school_list.html', context)


def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    context = {
        'teacher': teacher,
    }
    return render(request, 'pages/teacher_detail.html', context)
def student_grade(request, student_id):
    student = Student.objects.get(id=student_id)
    grades = student.grade_set.all()
    context = {
        'student': student,
        'grades': grades,
    }
    return render(request, 'pages/student_grade.html', context)


def class_schedule(request, class_id):
    class_obj = Class.objects.get(id=class_id)
    lessons = class_obj.lesson_set.all()
    context = {
        'class': class_obj,
        'lessons': lessons,
    }
    return render(request, 'pages/class_schedule.html', context)
