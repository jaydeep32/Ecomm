from django.shortcuts import render
from django.http import JsonResponse
from cart.models import Cart, ProductInCart
from product.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def get_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, ordered=False).first()
        return {
            'cart': cart,
        }
    return


@login_required
def view_cart(request):
    context = get_cart(request)
    return render(request, 'cart/cart.html', context)


@login_required
def checkout(request):
    context = get_cart(request)
    return render(request, 'cart/checkout.html', context)


@login_required
def confirmation(request):
    context = get_cart(request)
    cart = context.get('cart')
    cart.ordered = True
    cart.save()
    cart.save_order
    return render(request, 'cart/confirmation.html', context)


@login_required
def add_to_cart(request, slug):
    data = request.POST
    cart, _ = Cart.objects.get_or_create(user=request.user, ordered=False)
    qty = int(data.get('qty', 1))
    product = Product.objects.get(slug=slug)
    if cart and product.qty >= qty:
        product.qty -= qty
        product.save()
        product_in_cart, created = ProductInCart.objects.get_or_create(cart=cart, product=product)
        product_in_cart.qty += qty
        product_in_cart.save()
    
    return JsonResponse("Done", safe=False)
