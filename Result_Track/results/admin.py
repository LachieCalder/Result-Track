from django.contrib import admin

from results.models import *

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class ResultAdmin(admin.ModelAdmin):
    pass
admin.site.register(Result, ResultAdmin)

class AssignmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Assignment, AssignmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)

class TeacherAdmin(admin.ModelAdmin):
    pass
admin.site.register(Teacher, TeacherAdmin)

# Register your models here.
