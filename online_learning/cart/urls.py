from django.urls import path
from .views import *
urlpatterns = [
    path('cart/add/<int:course_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/remove/<int:cart_item_id>/',
         remove_from_cart, name='remove_from_cart'),
]
