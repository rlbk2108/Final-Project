from django.db import models
from core.models import Product
from django.contrib.auth.models import User
from datetime import datetime

CATEGORY = (
    ('print', 'Принтер'),
    ('proj', 'Проектор'),
    ('laptop', 'Ноутбук'),
)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField('Название товара', max_length=100)
    category = models.CharField('Категория', max_length=10, default='print', choices=CATEGORY)
    product_number = models.IntegerField('Количество товара', default=0)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

