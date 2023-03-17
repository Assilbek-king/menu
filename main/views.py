from main.models import *
from django.shortcuts import render
# Create your views here.

def indexHandler(request):
    products = Product.objects.filter(status=True)
    categories = Category.objects.filter(status=True)
    return render(request, 'menu.html', {
        'products': products,
        'categories': categories,
    })

