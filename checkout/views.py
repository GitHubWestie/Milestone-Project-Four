from django.shortcuts import render
from basket.basket import Basket

# Create your views here.
def checkout(request):
    basket = Basket(request)

    context = {
        'basket' : basket,
    }

    return render(request, 'checkout/checkout.html', context)