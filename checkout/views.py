import stripe
from basket.basket import Basket
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from courses.models import Course, Enrollment
from users.models import CustomUser
from django.utils import timezone

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def checkout(request):
    base_url = request.build_absolute_uri('/')
    success_url=f"{base_url}checkout/success?session_id={{CHECKOUT_SESSION_ID}}"
    cancel_url=f"{base_url}checkout/cancel/"
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
            success_url=success_url,
            cancel_url=cancel_url,
        )

        return redirect(checkout_session.url, code=303)

    context = {
        'basket' : basket,
    }

    return render(request, 'checkout/checkout.html', context)


def success(request):
    """
    Check for payment confirmation in Stripe session and if it exists enrol 
    user in purchased course.
    If not redirect back to basket to complete checkout.
    """

    basket = Basket(request)
    user = request.user

    # Get session_id from success URL
    session_id = request.GET.get('session_id')

    if not session_id:
        # If no session_id in URL send user back to basket
        return redirect(reverse('view_basket'))

    # Get stripe session with session_id
    checkout_session = stripe.checkout.Session.retrieve(session_id)

    if checkout_session.payment_status == 'paid':
        # Enroll user in purchased course/s
        for item in basket:
            Enrollment.objects.create(
                user = user,
                course = item['course'],
                enrolled_at = timezone.now(),
            )

        basket.clear()

        return render(request, 'checkout/success.html')
    else:
        return redirect('basket.html')


def cancel(request): 

    return render(request, 'checkout/cancel.html')