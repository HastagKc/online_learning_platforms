from .models import Course, Cart
import requests
import json
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import CartItem
from django.shortcuts import get_object_or_404, redirect


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


# payment form
def payement_form(request, cartItem_id):
    # getting specific cartItem
    cartItem = get_object_or_404(CartItem, id=cartItem_id)

    # getting course name
    course = cartItem.course

    # getting course price
    amount = cartItem.course.price

    # user associated with cartItem
    user = cartItem.cart.user

    context = {
        'cartItem': cartItem,
        'course': course,
        'amount': amount,
        'user': user,
    }

    return render(request, 'cart/payment_form.html', context=context)


# payment
@login_required
@csrf_exempt
def init_khalti(request, id):
    cartItem = get_object_or_404(CartItem, id=id)
    url = "https://a.khalti.com/api/v2/epayment/initiate/"
    return_url = 'http://127.0.0.1:8000/cart/verify/'
    website_url = 'http://127.0.0.1:8000/cart/verify/'
    amount = cartItem.course.price
    transaction_id = str(uuid.uuid4())
    purchase_order_name = cartItem.course.course_title
    user = cartItem.cart.user

    payload = json.dumps({
        "return_url": return_url,
        "website_url": website_url,
        "amount": amount,
        "purchase_order_id": cartItem.id,
        "purchase_order_name": purchase_order_name,
        "transaction_id": transaction_id,
        "customer_info": {
            "name": user.username,
            "email": user.email,
            "phone": "9800000010",  # Ideally, retrieve the actual phone number
        },
        "product_details": [
            {
                "identity": cartItem.id,
                "name": purchase_order_name,
                "unit_price": amount,
                "total_price": amount,
                "quantity": 1
            }
        ],
        "merchant_username": user.username,
    })

    headers = {
        'Authorization': 'Key 4af23dc17ef244338b43239b43a3d8e1',
        'Content-Type': 'application/json',
    }

    response = requests.post(url, headers=headers, data=payload)
    new_res = response.json()

    if response.status_code == 200 and 'payment_url' in new_res:
        return redirect(new_res['payment_url'])
    else:
        return JsonResponse({'error': 'Failed to initiate payment', 'details': new_res}, status=400)
