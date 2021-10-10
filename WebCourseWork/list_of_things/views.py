from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from list_of_things.models import Product


class ListView(View):
    """Список Товаров"""
    def get(self, request):
        product = Product.objects.all()
        return render(request, "list_of_things/product_list.html", {"product_list": product})