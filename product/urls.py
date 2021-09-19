from django.urls import path
from product import views
from django.views.generic import TemplateView

app_name = 'product'

urlpatterns = [
    path('', views.index, name='home'),
    path('product/<slug:slug>/', views.product_detail, name='product-detail'),
    path('category/<slug:slug>/<str:price>/<str:sort>/', views.category_products, name='category-products'),
    path('product/search12/', views.search_products, name='search-products'),
    path('products/', views.category, name='category-products'),
    path('contact/', TemplateView.as_view(template_name='product/contact.html'), name='contact'),
]


