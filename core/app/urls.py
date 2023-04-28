from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("about/", views.about, name="about"),
    # path('timetable/', views.timetable, name='timetable'),
    # path('teacher_timetable/<int:id>/', views.teacher_timetable, name='teacher_timetable'),

]
