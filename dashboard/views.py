from django.shortcuts import render

# Create your views here.
def dash(request):
    """ Get user data to display Welcome message """

    user_data = request.user
    return render(request, 'dashboard/dashboard.html', {'key':user_data})