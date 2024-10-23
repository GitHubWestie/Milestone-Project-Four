from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django.shortcuts import get_object_or_404
from .forms import CourseForm, LessonFormset
from django.contrib.auth.decorators import login_required


@login_required
def course_admin(request):
    """ Get course list for authenticated admin users """
    user = request.user

    if not user.is_superuser and not user.is_staff:
        return redirect('dashboard')

    try:
        courses = Course.objects.all()

        context = {
            'courses': courses
        }

        return render(request, 'administration/course-admin.html', context)
    except Exception as e:
        print({e})
        return render(request, 'error.html', {'error': {e}})


@login_required
def add_course(request):
    """ Allow authenticated admins to add new courses """
    user = request.user

    if not user.is_superuser and not user.is_staff:
        return redirect('dashboard')

    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        if course_form.is_valid():
            course_form.save()
            return redirect('course_admin')
    else:
        course_form = CourseForm()

    context = {
        'course_form': course_form
    }

    return render(request, 'administration/add-course.html', context)


@login_required
def edit_course(request, pk):
    """ Allow authenticated admins to edit courses and add/edit lessons """
    user = request.user

    if not user.is_superuser and not user.is_staff:
        return redirect('dashboard')

    course = get_object_or_404(Course, pk=pk)
    lessons = Lesson.objects.filter(course_id=course.pk)

    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES, instance=course)
        lesson_form = LessonFormset(request.POST,
                                    queryset=lessons, instance=course)

        if course_form.is_valid() and lesson_form.is_valid():
            course_form.save()
            lesson_form.save()
            return redirect('edit_course', pk=pk,)

    else:
        course_form = CourseForm(instance=course)
        lesson_form = LessonFormset(queryset=lessons, instance=course)

    context = {
        'course': course,
        'course_form': course_form,
        'lesson_form': lesson_form,
    }

    return render(request, 'administration/edit-course.html', context)


@login_required
def delete_course(request, pk):
    """ Allow authenticated admins to delete courses """
    user = request.user

    if not user.is_superuser and not user.is_staff:
        return redirect('dashboard')

    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_admin')

    return render(request, 'administration/course-admin.html')
