from django.shortcuts import render
from django.views.generic import ListView

from .models import AllProd

class ProductListView(ListView):
    model = AllProd
    context_object_name = 'products'
    template_name = 'product/all_products.html'
