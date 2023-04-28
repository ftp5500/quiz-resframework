from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from datetime import date

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(_("الاسم الأول"), max_length=30, blank=True)
    mid_name = models.CharField(_("اسم الأب"), max_length=30, blank=True)
    last_name = models.CharField(_("اسم العائلة"), max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'المستخدم'
        verbose_name_plural = 'المستخدمون'

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.mid_name} {self.last_name}"
        return self.email

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.get_full_name()


# Create your models here.
STUDENT_LEVEL = [
    ("الأول ابتدائي", "الأول ابتدائي"),
    ("الثاني ابتدائي", "الثاني ابتدائي"),
    ("الثالث ابتدائي", "الثالث ابتدائي"),
    ("الرابع ابتدائي", "الرابع ابتدائي"),
    ("الخامس ابتدائي", "الخامس ابتدائي"),
    ("السادس ابتدائي", "السادس ابتدائي"),
    ("الأول متوسط", "الأول متوسط"),
    ("الثاني متوسط", "الثاني متوسط"),
    ("الثالث متوسط", "الثالث متوسط"),
    ("الأول ثانوي", "الأول ثانوي"),
    ("الثاني ثانوي", "الثاني ثانوي"),
    ("الثالث ثانوي", "الثالث ثانوي"),
]

SUBJECTS_LIST = (
    ("قران", "قران"),
    ("تربية اسلامية", "تربية اسلامية"),
    ("لغتي", "لغتي"),
    ("رياضيات", "رياضيات"),
    ("علوم", "علوم"),
    ("تربية بدنية", "تربية بدنية"),
    ("تربية فنية", "تربية فنية"),
    ("لغة انجليزية", "لغة انجليزية"),
    ("اجتماعيات", "اجتماعيات"),
    ("مهارات حيايتة وأسرية", "مهارات حيايتة وأسرية"),
    ("التربية الرقمية", "التربية الرقمية"),

)

SECTIONS = [
    ("أ", "أ"),
    ("ب", "ب"),
    ("ج", "ج"),
    ("د", "د"),
]

SEMESTER = [
    ("الفصل الدراسي الأول", "الفصل الدراسي الأول"),
    ("الفصل الدراسي الثاني", "الفصل الدراسي الثاني"),
    ("الفصل الدراسي الثالث", "الفصل الدراسي الثالث"),
]

DAYS_OF_WEEK = (
    ("0", 'الأحد'),
    ("1", 'الأثنين'),
    ("2", 'الثلاثاء'),
    ("3", 'الأربعاء'),
    ("4", 'الخميس'),
)

CLASS_TIME = [
    ("1", "الحصة الأولى"),
    ("2", "الحصة الثانية"),
    ("3", "الحصة الثالثة"),
    ("4", "الحصة الرابعة"),
    ("5", "الحصة الخامسة"),
    ("6", "الحصة السادسة"),
    ("7", "الحصة السابعة"),
    ("8", "الحصة الثامنة"),
    ("9", "الحصة التاسعة"),
]


#
#
# class ClassTime(models.Model):
#     title = models.CharField(_('الحصة'), choices=CLASS_TIME, max_length=150)
#     starting = models.TimeField(_('بداية الحصة'), null=True)
#     ending = models.TimeField(_('نهاية الحصة'), null=True)
#
#     class Meta:
#         verbose_name = 'الحصة'
#         verbose_name_plural = 'الحصص'
#         ordering = ['title', 'starting']
#
#     def __str__(self):
#         return f"{self.get_title_display()} - ({self.starting}-{self.ending})"
#
#
# class Timetable(models.Model):
#     day = models.CharField(_('اليوم'), max_length=50, choices=DAYS_OF_WEEK)
#     class_time = models.ManyToManyField(ClassTime, related_name='class_time')
#
#     class Meta:
#         verbose_name = 'جدول الحصص'
#         verbose_name_plural = 'جدول الحصص'
#         ordering = ['day']
#
#
#
#     def __str__(self):
#         return f"{self.get_day_display()} "
#
#
#
#
# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.PROTECT)
#     is_teacher = models.BooleanField(default=True)
#     major = models.CharField(_("التخصص"), max_length=100, choices=SUBJECTS_LIST, null=True)
#
#     class Meta:
#         verbose_name = "المعلم- Teacher"
#         verbose_name_plural = "المعلمون- Teachers"
#
#     def __str__(self):
#         return f"{self.user} "
#
#
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_student = models.BooleanField(default=True)
#     age = models.IntegerField(_("العمر"), blank=True, null=True)
#
#     class Meta:
#         verbose_name = "الطالب - Student"
#         verbose_name_plural = "الطلاب - Students"
#
#     def __str__(self):
#         return f"{self.user}"
#
#
# #
# class Subject(models.Model):
#     name = models.CharField(_("المادة"), max_length=255, choices=SUBJECTS_LIST)
#     code = models.CharField(_("رمز المادة"), max_length=10, default="")
#     teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)
#
#
#     def __str__(self):
#         return f" {self.name} - {self.teacher} "
#
#     class Meta:
#         verbose_name = "المادة الدراسية - Subject"
#         verbose_name_plural = "المواد الدراسية - Subjects"
#
#
# class Class(models.Model):
#     name = models.CharField(_("الصف"), max_length=150, choices=STUDENT_LEVEL)
#     students = models.ManyToManyField(Student, related_name="classes")
#     section = models.CharField(_("الشعبة"), max_length=2, choices=SECTIONS)
#
#     class Meta:
#         verbose_name = 'الفصل - Class'
#         verbose_name_plural = "الفصول - Classes"
#
#     def __str__(self):
#         return f"{self.name} - {self.section}"
#
#
# class SchoolClass(models.Model):
#     class_group = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, related_name=_('الصف'))
#     class_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
#     class_time = models.ForeignKey(Timetable, on_delete=models.CASCADE, null=True)
#
#     class Meta:
#         verbose_name = 'School Class - الحصة الدراسية'
#         verbose_name_plural = 'الحصص الدراسية -  School Classes '
#         ordering = ['class_time']
#
#     # def get_class_time(self):
#     #     return self.get_class_time_display()
#
#     def __str__(self):
#         return f" {self.class_time} - {self.class_subject}"
#
#
# class Course(models.Model):
#     COURSE_METHODS = (
#         ("عصف ذهني", "عصف ذهني"),
#         ("خرائط ذهنية", "خرائط ذهنية"),
#         ("الصف المقلوب", "الصف المقلوب"),
#         ("التعلم التعاوني", "التعلم التعاوني"),
#         ("التعلم الذاتي", "التعلم الذاتي"),
#         ("التجارب", "التجارب")
#     )
#     name = models.CharField(max_length=150)
#     teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
#     subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
#     which_class = models.OneToOneField(Class, on_delete=models.CASCADE, blank=False, null=True)
#     my_column = MultiSelectField(choices=COURSE_METHODS, null=True)
#
#     description = models.TextField()
#
#     class Meta:
#         verbose_name = "الدرس - Course"
#         verbose_name_plural = "الدروس - Courses"
#
#     def __str__(self):
#         return f"{self.name} - {self.which_class}"
#
#
# class Semester(models.Model):
#     name = models.CharField(max_length=50, choices=SEMESTER)
#     start_date = models.DateField()
#     end_date = models.DateField()
#
#     class Meta:
#         verbose_name = 'الفصل الدراسي'
#         verbose_name_plural = 'الفصول الدراسية'
#
#     def __str__(self):
#         return self.name
#
#
# class Assignment(models.Model):
#     name = models.CharField(max_length=100)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     due_date = models.DateTimeField()
#     description = models.TextField()
#
#     class Meta:
#         verbose_name = 'الواجب - Assignment'
#         verbose_name_plural = 'الواجبات - Assignments'
#
#     def __str__(self):
#         return f"{self.name} - {self.course}"
#
#
# class Grade(models.Model):
#     assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = 'درجة الواجب - Assignment Grade'
#         verbose_name_plural = 'درجة الواجبات - Assignments Grades'
#
#     def __str__(self):
#         return self.assignment
#
#
# class Quizzes(models.Model):
#     title = models.CharField(max_length=150, null=True, default=_("اختبار جديد"), verbose_name=_("عنوان الاختبار"))
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#
#     class Meta:
#         verbose_name = _('الاختبار - Quiz')
#         verbose_name_plural = _('الاختبارات - Quizzes')
#         ordering = ["course"]
#
#     def __str__(self):
#         return f"{self.title} - {self.course}"
#
#
# class Updated(models.Model):
#     date_updated = models.DateTimeField(verbose_name=_('آخر تحديث'), auto_now_add=True)
#
#     class Meta:
#         abstract = True
#
#
# class Question(models.Model):
#     SCALE = (
#         (0, _("Fundamental")),
#         (1, _("Beginner")),
#         (2, _("Intermediate")),
#         (3, _("Advanced")),
#         (4, _("Expert")),
#     )
#
#     TYPE = (
#         (0, _('Multiple Choice')),
#     )
#     title = models.CharField(max_length=255, verbose_name=_("Title"))
#     technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of Question"))
#     quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE, null=True, related_name="question")
#     difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_('Difficulty'))
#     created = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=False, verbose_name=_('Active Status'))
#
#     class Meta:
#         verbose_name = _('السؤال - Question')
#         verbose_name_plural = _('الاسئلة - Questions')
#         ordering = ["id"]
#
#     def __str__(self):
#         return f"{self.title} - {self.quiz.course}"
#
#
# class Answer(Updated):
#     question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('بيانات المدرسة - School Data')
        verbose_name_plural = _('بيانات المدرسة - School Data')
        
    def __str__(self):
        return f"{self.name}"

class Teacher(User):
    major = models.CharField(_('التخصص') , max_length=150, choices=SUBJECTS_LIST, null=True)

    class Meta:
        verbose_name = _('المعلم - Teacher')
        verbose_name_plural = _('المعلمون - Teachers')
        ordering = ['first_name']

    def __str__(self):
        return f"{self.get_full_name()}"


class Student(User):
    birthdate = models.DateField()



    class Meta:
        verbose_name = _('الطالب - Student')
        verbose_name_plural = _('الطلاب - Students')
        ordering = ['first_name']

    def __str__(self):
        return f"{self.get_full_name()}"
