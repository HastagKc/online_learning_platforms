from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Cart, CartItem


@login_required
def add_to_cart(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the course is already in the cart
    cart_item_exists = CartItem.objects.filter(
        cart=cart, course=course).exists()

    if not cart_item_exists:
        CartItem.objects.create(cart=cart, course=course)

    return redirect('view_cart')


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'cart': cart,
        'items': cart.items.all(),
    }
    return render(request, 'cart/view_cart.html', context)


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')
