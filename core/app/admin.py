from django.contrib import admin
from datetime import date
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','get_full_name','birthdate', 'age')
    def age(self, obj):
        today = date.today()
        age = today.year - obj.birthdate.year - ((today.month, today.day) < (obj.birthdate.month, obj.birthdate.day))
        return age

    age.short_description = 'العمر'

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','get_full_name', 'major')

    def full_name(self, obj):
        return obj.get_full_name().upper()
    full_name.short_description =  'الاسم'


class ClassAdmin(admin.ModelAdmin):
    list_display = ['id','name','start_at','end_at']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','name','teacher']


    def subjectTeacher(self ,obj):
        return f"{obj.get_full_name().upper()}"
    subjectTeacher.short_description = 'معلم المادة'

class GradeAdmin(admin.ModelAdmin):
    list_display = ['id','name','section']

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['student'] = None
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id','class_is','subject']

admin.site.register(User)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Lesson, LessonAdmin)


