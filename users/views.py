from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    """ Display dashboard and make user session data available """
    user = request.user

    return render(request, 'users/dashboard.html', {'user' : user})