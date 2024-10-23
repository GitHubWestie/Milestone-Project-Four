from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import CustomUser, UserProfile
from .forms import CustomUserForm, UserProfileForm
from django.shortcuts import get_object_or_404


@login_required
def dashboard(request):
    """ Get user data to display welcome message and enrolled courses """
    try:
        complete_user = CustomUser.objects.select_related(
            'profile').get(id=request.user.id)

        enrolled_courses = request.user.enrollments.all()

        context = {
            'complete_user': complete_user,
            'enrolled_courses': enrolled_courses,
        }

        return render(request, 'users/dashboard.html', context)
    except Exception as e:
        print({e})
        return render(request, 'error.html', {'error': {e}})



@login_required
def edit_profile(request):
    """
    Get existing user data and pre-fill form instances for editing profile
    On submission, save updated user profile
    """
    try:
        user = request.user
        profile, created = UserProfile.objects.get_or_create(user=user)

        if request.method == 'POST':
            user_form = CustomUserForm(request.POST, instance=user)
            profile_form = UserProfileForm(
                request.POST, request.FILES, instance=profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('dashboard')

        else:
            # Fill the forms with existing data
            user_form = CustomUserForm(instance=user)
            profile_form = UserProfileForm(instance=profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(request, 'users/edit-profile.html', context)
    except Exception as e:
        print({e})
        return render(request, 'error.html', {'error': {e}})
