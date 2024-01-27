from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''
        
    return HttpResponse('Welcome to 6410742016 Apisit Sangkrajang views!')

def item_view(request, item_id):   
    context_data = {
        "item_id" : item_id   
        }
    
    return render(request, 'index.html', context_data)

def category_view(request):   
    '''This function render category page of ecommerce views'''
    
    return render(request, 'category.html')

def checkout_view(request):   
    '''This function render checkout page of ecommerce views'''
    
    return render(request, 'checkout.html')

def contact_view(request):
    '''This function render contact page of ecommerce views'''
    
    return render(request, 'contact.html')

def home_view(request):
    '''This function render home page of ecommerce views'''
    
    return render(request, 'home.html')

def product_view(request):
    '''This function render product page of ecommerce views'''
    
    return render(request, 'product.html')