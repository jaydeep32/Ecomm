from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_popular = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'

    @property
    def total_product(self):
        return self.products.count()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField()
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    pic = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_discount = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    qty = models.IntegerField(default=2)
    created_at = models.DateField(auto_now_add=True)

    @property
    def get_price(self):
        if self.is_discount:
            return self.price - (self.price * self.discount) / 100
        return self.price

    @property
    def in_stock(self):
        if self.qty > 1:
            pass

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



