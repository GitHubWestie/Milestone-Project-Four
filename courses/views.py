from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from . models import Course, Lesson, Enrollment
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def get_courses(request):
    """ Gets all courses for the courses template """

    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses':courses})


@login_required
def get_lesson(request, uuid):
    """ Access course content if user is enrolled on course """

    lesson = get_object_or_404(Lesson, uuid=uuid)

    if not Enrollment.objects.filter(user=request.user, course=lesson.course_id).exists():
        return HttpResponseForbidden('You need to purchase this course before you can access its content')

    next_lesson = Lesson.objects.filter(
        course_id=lesson.course_id, order__gt=lesson.order).order_by('order').first()
    previous_lesson = Lesson.objects.filter(
        course_id=lesson.course_id, order__lt=lesson.order).order_by('-order').first()

    context = {
        'lesson':lesson,
        'next_lesson':next_lesson,
        'previous_lesson':previous_lesson,
    }

    return render(request, 'courses/lesson.html', context)