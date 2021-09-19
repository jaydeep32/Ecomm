import product
from django.db import models
from django.conf import settings
from product.models import Product


User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    @property
    def save_order(self):
        self.products.all().update(ordered=True)

    @property
    def subtotal(self):
        return sum(i.get_total for i in self.products.all())

    def __str__(self):
        return self.user.username


class ProductInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_in_cart')
    ordered = models.BooleanField(default=False)
    qty = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    @property
    def get_total(self):
        price = self.product.get_price
        return self.qty * price

    def __str__(self):
        return f"{self.product} - {self.cart.user}"
    

