from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(ClassGroup)

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Grade)
admin.site.register(Semester)
admin.site.register(Quizzes)
admin.site.register(Question)

