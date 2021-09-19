from django.urls import path
from cart import views
from django.views.generic import TemplateView


app_name = 'cart'

urlpatterns = [
    path('cart/', views.view_cart, name='view-cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('add/<slug:slug>/', views.add_to_cart, name='add-cart'),
]


