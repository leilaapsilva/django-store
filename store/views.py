from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.template import loader

def index(request):

    #returns a list of the 5 latest products
    latest_products_list = Product.objects.order_by('-creation_date')[:5]
    #template = loader.get_template('store/index.html')
    context = {
        'latest_products_list': latest_products_list,
    }
    
    #output = ', '.join([p.name for p in latest_products_list])

    return render(request, 'store/index.html', context)

#information about product
def detail(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)    

