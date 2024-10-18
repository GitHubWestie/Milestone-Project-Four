from django import forms
from courses.models import Course, Lesson
from users.forms import CustomUserForm, UserProfileForm


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
        


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = [
            'title',
            'description',
            'video_url',
            'order',
        ]
