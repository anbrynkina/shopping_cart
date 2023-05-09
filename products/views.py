from django.shortcuts import render

# Create your views here.

# created a controller to show the page
def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

# to test how dynamic content works, creating test function
def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Welcome to the store!',
        'username': 'Anna',
    }
    return render(request, 'products/test_context.html', context)
