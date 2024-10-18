from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django.shortcuts import get_object_or_404
from .forms import CourseForm, LessonFormset
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def admin(request):
    user = request.user
    
    if not user.is_superuser and not user.is_staff:
        return redirect('dashboard')

    return render(request, 'administration/admin.html')


@login_required
def course_admin(request):
    user = request.user

    if not user.is_superuser and not user.is_staff:
        return redirect('dashboard')

    courses = Course.objects.all()

    return render(request, 'administration/course-admin.html', {'courses' : courses})


@login_required
def edit_course(request, pk):

    user = request.user

    if not user.is_superuser and not user.is_staff:
        return redirect('dashboard')

    course = get_object_or_404(Course, pk=pk)
    lessons = Lesson.objects.filter(course_id=course.pk)

    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES, instance=course)
        lesson_form = LessonFormset(request.POST, queryset=lessons, instance=course)

        if course_form.is_valid and lesson_form.is_valid:
            course_form.save()
            lesson_form.save()
            return redirect('course_admin')

    else:
        course_form = CourseForm(instance=course)
        lesson_form = LessonFormset(queryset=lessons, instance=course)

    context = {
        'course_form' : course_form,
        'lesson_form' : lesson_form,
    }

    return render(request, 'administration/edit-course.html', context)