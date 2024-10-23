from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from . models import Course, Lesson, Enrollment
from django.http import HttpResponseForbidden
from django.contrib import messages


@login_required
def get_courses(request):
    """ Gets all courses for the courses template """
    try:
        courses = Course.objects.all()
        return render(request, 'courses/courses.html', {'courses': courses})
    except Exception as e:
        print({e})
        return render(request, 'error.html', {'error': {e}})


@login_required
def get_lesson(request, uuid):
    """ Access course content if user is enrolled on course """
    try:
        lesson = get_object_or_404(Lesson, uuid=uuid)

        if not Enrollment.objects.filter(
                user=request.user, course=lesson.course_id).exists():
            messages.error(
                request,
                'Purchase a course to access its content')
            return redirect('get_courses')

        next_lesson = Lesson.objects.filter(
            course_id=lesson.course_id, order__gt=lesson.order).order_by(
            'order').first()
        previous_lesson = Lesson.objects.filter(
            course_id=lesson.course_id, order__lt=lesson.order).order_by(
            '-order').first()

        context = {
            'lesson': lesson,
            'next_lesson': next_lesson,
            'previous_lesson': previous_lesson,
        }

        return render(request, 'courses/lesson.html', context)
    except Exception as e:
        print({e})
        return render(request, 'error.html', {'error': {e}})
