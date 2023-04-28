from django.contrib import admin
from datetime import date
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_full_name','birthdate', 'age')
    def age(self, obj):
        today = date.today()
        age = today.year - obj.birthdate.year - ((today.month, today.day) < (obj.birthdate.month, obj.birthdate.day))
        return age

    age.short_description = 'العمر'

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'major')

    def full_name(self, obj):
        return obj.get_full_name().upper()
    full_name.short_description =  'الاسم'









admin.site.register(User)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)


