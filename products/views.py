from django.shortcuts import render

# Create your views here.

# created a controller to show the page
def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')