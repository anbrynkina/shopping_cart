from django.shortcuts import render

# Create your views here.

# created a controller to show the page
def index(request):
    context = {
        'title': 'Store Homepage'
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Products Catalogue'
    }
    return render(request, 'products/products.html', context)

# to test how dynamic content works, creating test function
def test_context(request):
    context = {
        'title': 'store',
        'header': 'Welcome to the store!',
        'username': 'Anna',
        'products': [
            {'name': 'adidas Original Black Monogram Hoodies', 'price': 80},
            {'name': 'The North Face blue jacket', 'price': 100},
            {'name': 'ASOS DESIGN oversize sports top in brown', 'price': 59.9},
        ],
        # 'promotion': True,
        'products_of_promotion': [
            {'name': 'Nike Black Heritage Backpack', 'price': 69},
        ]
    }
    return render(request, 'products/test_context.html', context)
