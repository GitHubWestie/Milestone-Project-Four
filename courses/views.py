from django.shortcuts import render, get_object_or_404
from . models import Course, Lesson

# Create your views here.
def get_courses(request):
    """ Gets all courses for the courses template """

    courses = Course.objects.all()

    return render(request, 'courses/courses.html', {'courses':courses})


def get_lesson(request, uuid):
    
    lesson = get_object_or_404(Lesson, uuid=uuid)

    next_lesson = Lesson.objects.filter(order__gt=lesson.order).order_by('order').first()
    previous_lesson = Lesson.objects.filter(order__lt=lesson.order).order_by('-order').first()

    context = {
        'lesson':lesson,
        'next_lesson':next_lesson,
        'previous_lesson':previous_lesson,
    }

    return render(request, 'courses/lesson.html', context)