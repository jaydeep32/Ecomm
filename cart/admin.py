from django.contrib import admin
from cart.models import Cart, ProductInCart

# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "no_of_products", "ordered", "created_at",]

    def no_of_products(self, query):
        return query.products.count()


@admin.register(ProductInCart)
class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ["cart", "product", "qty", "created_at",]