from django import template
from cart.models import Cart
from product.models import Product
import random


register = template.Library()

@register.simple_tag()
def cart_couner(request):
    if not request.user.is_anonymous:
        cart = Cart.objects.filter(user=request.user, ordered=False).first()
        if cart:
            return cart.products.count()
    return 0


@register.inclusion_tag('product/gallery.html')
def gallery():
    products = Product.objects.all()
    products = [i for i in products][:50]
    random.shuffle(products)
    return {
        'products': products[:10], 
    }

