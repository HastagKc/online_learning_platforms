from django.db import models
from accounts.models import CustomUserModel
from online_learning_app.models import Course


# model
# cart model
# Cart represents the overall course cart for a user.
class Cart(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart {self.id} for {self.user.username}'


# cartItem Model
# CartItem represents individual items within that cart.
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.course.course_title} in cart {self.cart.id}'
