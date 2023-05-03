from django.shortcuts import render
from .models import Teacher , Class , Grade


# Create your views here.
def index(request, *args, **kwargs):
    return render(request, "pages/index.html")


def about(request, *args, **kwargs):
    classes = Class.objects.all()
    data = {
        "classes": classes
    }
    print(data)
    return render(request, "pages/about.html" , data)
#
def timetable(request ):
    grades = Grade.objects.all()
    context = {'grades': grades}
    return render(request, 'pages/timetable.html', context)
#
# def teacher_timetable(request , id):
#     course = SchoolClass.objects.filter(class_subject__teacher__user_id=id)
#     context = {'course':course}
#     return render(request , 'pages/teacher_timetable.html' , context)

