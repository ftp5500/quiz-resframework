from django.shortcuts import render
from .models import Teacher , ClassGroup , SchoolClass


# Create your views here.
def index(request, *args, **kwargs):
    return render(request, "pages/index.html")


def about(request, *args, **kwargs):
    classes = ClassGroup.objects.all()
    data = {
        "classes": classes
    }
    print(data)
    return render(request, "pages/about.html" , data)

def timetable(request):
    courses = SchoolClass.objects.all()
    context = {'courses': courses}
    return render(request, 'pages/timetable.html', context)