from django.shortcuts import render, get_object_or_404
from . models import Course, Lesson

# Create your views here.
def get_courses(request):
    """ Gets all courses for the courses template """

    courses = Course.objects.all()

    return render(request, 'courses/courses.html', {'courses':courses})


def get_lesson(request, uuid):
    
    lesson = get_object_or_404(Lesson, uuid=uuid)

    return render(request, 'courses/lesson.html', {'lesson':lesson})