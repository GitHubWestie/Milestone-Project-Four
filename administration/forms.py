from django import forms
from courses.models import Course, Lesson
from django.forms.models import inlineformset_factory


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'price',
            'category',
            'cover_image',
            'instructor',
        ]


LessonFormset = inlineformset_factory(
    Course, Lesson,
    fields=(
        'title',
        'description',
        'video_url',
        'order',
    ),
    extra=1,
    can_delete=True
)
