from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from . models import Course, Lesson

@login_required
# Create your views here.
def get_courses(request):
    """ Gets all courses for the courses template """

    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses':courses})


@login_required
def get_lesson(request, uuid):
    """  """

    lesson = get_object_or_404(Lesson, uuid=uuid)
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