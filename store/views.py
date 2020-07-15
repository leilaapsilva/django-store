from django.shortcuts import render, get_object_or_404

from .models import Product

def index(request):

    #returns a list of the 5 latest products
    latest_products_list = Product.objects.order_by('-creation_date')[:5]
    context = {
        'latest_products_list': latest_products_list,
    }
    
    return render(request, 'store/index.html', context)

#information about product
def detail(request, product_id):
    #404 error if product does not exist
    product = get_object_or_404(Product, id=product_id)     

    return render(request, 'store/detail.html', {'product': product})    

