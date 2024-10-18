from django.shortcuts import render, redirect
from users.models import CustomUser, UserProfile
from courses.models import Course, Lesson
from .forms import CustomUserForm, UserProfileForm
from django.shortcuts import get_object_or_404

# Create your views here.
def admin(request):
    user = request.user
    
    if user.is_superuser or user.is_staff:
        users = CustomUser.objects.select_related('profile').all()

        return render(request, 'administration/admin.html')
    else:
        return redirect('dashboard')