from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from courses.models import Course
from . basket import Basket


# Create your views here.
def view_basket(request):
    basket = Basket(request)
    total = basket.basket_total()

    context = {
        'basket' : basket,
        'total' : total,
    }

    for item in basket:
        print(item)

    return render(request, 'basket/basket.html', context)


def add_to_basket(request, course_id):
    basket = Basket(request)
    course = get_object_or_404(Course, id=course_id)
    basket.add(course=course)

    return redirect(reverse('view_basket'))


def remove_from_basket(request, course_id):
    basket = Basket(request)
    course = get_object_or_404(Course, id=course_id)
    basket.remove(course)
    return redirect(reverse('view_basket'))
