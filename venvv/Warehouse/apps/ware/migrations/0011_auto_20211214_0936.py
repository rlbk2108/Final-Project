# Generated by Django 3.2.9 on 2021-12-14 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ware', '0010_alter_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_product_name',
        ),
        migrations.AddField(
            model_name='order',
            name='order_product_name',
            field=models.ManyToManyField(null=True, to='ware.Product'),
        ),
    ]
