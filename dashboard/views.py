from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import CustomUser, UserProfile

# Create your views here.

@login_required
def dash(request):
    """ Get user data to display Welcome message """

    complete_user = CustomUser.objects.select_related(
        'profile').get(id=request.user.id)

    enrolled_courses = request.user.enrollments.all()

    course_titles = []
    for courses in enrolled_courses:
        course_titles.append(courses.course.title)

    context = {
        'complete_user' : complete_user,
        'course_titles' : course_titles,
    }

    return render(request, 'dashboard/dashboard.html', context)