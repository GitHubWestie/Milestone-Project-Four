import stripe
from basket.basket import Basket
from django.conf import settings
from django.shortcuts import render, redirect

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def checkout(request):
    basket = Basket(request)

    if request.method == 'POST':
        line_items = []

        for item in basket:
            line_items.append({
                'price_data' : {
                    'currency' : 'gbp',
                    'product_data' : {
                        'name' : item['course'].title,
                    },
                    'unit_amount' : int(item['price'] * 100),
                },
                'quantity' : 1,
            })

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url="https://animated-computing-machine-xjwqq45wqpv2vpr7-8000.app.github.dev/checkout/success/", 
            cancel_url="https://animated-computing-machine-xjwqq45wqpv2vpr7-8000.app.github.dev/checkout/cancel/", 
        )

        return redirect(checkout_session.url, code=303)

    context = {
        'basket' : basket,
    }

    return render(request, 'checkout/checkout.html', context)


def success(request):
    basket = Basket(request)

    basket.clear()

    return render(request, 'checkout/success.html')


def cancel(request):
    return render(request, 'checkout/cancel.html')