from django.views.generic import ListView
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404



from .extras import generate_order_id

import datetime

from .models import Order, Product, Profile

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/all_products.html'


def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0


@login_required()
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    product = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    if product.product_number > 1:
        quantity = product.product_number-1
        user_profile.ordered_product_num + quantity
        user_order.items.add(user_profile.ordered_product_num, product.product_name, product.date_ordered)
        user_profile.save()

    messages.info(request, "item added to cart")
    return redirect(reverse('ware:all_products'))


# @login_required()
# def delete_from_cart(request, item_id):
#     item_to_delete = OrderItem.objects.filter(pk=item_id)
#     if item_to_delete.exists():
#         item_to_delete[0].delete()
#         messages.info(request, "Item has been deleted")
#     return redirect(reverse('ware:order_summary'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'order/order_summary.html', context)


def my_profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter()
	context = {
		'my_orders': my_orders
	}

	return render(request, "profile/profile.html", context)
