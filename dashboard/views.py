from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dash(request):
    """ Get user data to display Welcome message """

    user_data = request.user
    return render(request, 'dashboard/dashboard.html', {'key':user_data})