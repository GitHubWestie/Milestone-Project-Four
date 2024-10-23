from django.contrib import admin
from .models import Course, Lesson, Enrollment


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Enrollment)
