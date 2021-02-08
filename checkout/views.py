from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I9Ba3HSPK4zEHFU5SiMgEg7inoLCkkJkFaZVssLTgTZkg5ORccM05U17zVKcgbkL0d5h4uLuEkvwtEsLA6qapUh00knX85Ttt',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
