from django.urls import path
from . import views

urlpatterns = [
    path('schools/', views.school_list, name='school_list'),
    path('teachers/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('students/<int:student_id>/grades/', views.student_grade, name='student_grade'),
    path('classes/<int:class_id>/schedule/', views.class_schedule, name='class_schedule'),
]
# handler404 = 'app.views.error_404'
