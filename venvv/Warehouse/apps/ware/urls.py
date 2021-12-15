from django.urls import path
from django.conf.urls import url
from django.urls.conf import re_path
from .views import ProductListView
from .import views
from .views import (
    add_to_cart,
    # delete_from_cart,
    my_profile
)

app_name = 'ware'

urlpatterns = [
    path('all-products/', ProductListView.as_view(), name='all_products'),
    path('profile/', views.my_profile, name="profile"),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name="add_to_cart"),
    path('all-products/order-summary', views.order_details, name="order_summary")
]
