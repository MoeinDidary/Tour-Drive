from django.shortcuts import render, redirect, get_object_or_404
from car_module.models import Car


def add_to_cart(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    cart = request.session.get('cart', {})

    if str(car_id) in cart:
        cart[str(car_id)] += 1
    else:
        cart[str(car_id)] = 1

    request.session['cart'] = cart

    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    cars = Car.objects.filter(id__in=cart.keys())

    cart_items = []
    total_price = 0

    for car in cars:
        quantity = cart[str(car.id)]
        total = car.price_per_hour * quantity
        total_price += total
        cart_items.append({
            'car': car,
            'quantity': quantity,
            'total': total
        })

    return render(request, 'order_module/cart-site.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def remove_from_cart(request, car_id):
    cart = request.session.get('cart', {})
    if str(car_id) in cart:
        del cart[str(car_id)]
        request.session['cart'] = cart
    return redirect('view_cart')
