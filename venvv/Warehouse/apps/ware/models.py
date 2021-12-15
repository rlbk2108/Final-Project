from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save


CATEGORY = (
    ('print', 'Принтер'),
    ('proj', 'Проектор'),
    ('laptop', 'Ноутбук'),
)

class Product(models.Model):
    product_name = models.CharField('Название товара', max_length=100)
    category = models.CharField('Категория', max_length=10, default='print', choices=CATEGORY)
    product_number = models.IntegerField('Количество товара', default=0)

    def __str__(self):
        return self.product_name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=CASCADE)
    order_product_name = models.ManyToManyField(Product, null=True)
    ordered_product_num = models.IntegerField("Количество занятого товара", default=0)
    date_ordered = models.DateTimeField(null=True)


    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    # def __str__(self):
    #     return self.owner

