from django.shortcuts import render, redirect
from product.models import Category, Product
from cart.models import ProductInCart
from django.contrib.auth.decorators import login_required


def index(request):
    category_qs = Category.objects.all()
    product_qs = Product.objects.all()
    best_seller = ProductInCart.objects.filter(ordered=True).order_by('-qty')[:10]
    context = {
        'categories': category_qs, 
        'products': product_qs, 
        'best_seller': best_seller, 
    }
    return render(request, 'index.html', context)


@login_required
def product_detail(request, slug):
    best_seller = ProductInCart.objects.filter(ordered=True).order_by('-qty')[:10]
    try:
        product = Product.objects.get(slug=slug)
    except:
        return redirect('product:home')
    else:
        context = {
            'best_seller': best_seller, 
            'product': product,
        }
        return render(request, 'product/single-product.html', context)


def category(request):
    best_seller = ProductInCart.objects.filter(ordered=True).order_by('-qty')[:10]
    try:
        category_qs = Category.objects.all()
        products = Product.objects.all()
    except:
        return redirect('product:home')
    else:
        context = {
            'products': products,
            'categories': category_qs, 
            'best_seller': best_seller, 
        }
        return render(request, 'product/category.html', context)


def category_products(request, slug, price=None, sort=None):
    if request.method == 'POST':
        if slug == 'None':
            products = Product.objects.all()
        else:
            try:
                products = Product.objects.filter(category__slug=slug)
            except:
                return redirect('product:home')
        if price == "None":
            products = products.order_by(sort)
        else:
            products = products.order_by(price)
        context = {
            'products': products,
        }
        return render(request, 'product/product_snippet.html', context)
    return redirect('product:home')


def search_products(request):
    # if request.method == 'POST':
    #     print("POST")
    #     search = request.POST.get('name')
    #     products = Product.objects.filter(name__icontains=search)
    #     context = {
    #         'products': products,
    #     }
    #     # return render(request, 'product/product_snippet.html', context)
    # print("GET")
    # return redirect('product:home12')
    pass

