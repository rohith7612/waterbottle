# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Sale
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

def home(request):
    return render(request, 'home.html')

def products(request):
    items = Product.objects.all()
    return render(request, 'products.html', {'products': items})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def admin_dashboard(request):
    products = Product.objects.all()
    sales = Sale.objects.all()
    return render(request, 'admin_dashboard.html', {'products': products, 'sales': sales})

@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        desc = request.POST['description']
        img = request.FILES['image']
        Product.objects.create(name=name, price=price, description=desc, image=img)
        messages.success(request, "Product added successfully")
        return redirect('admin_dashboard')
    return render(request, 'add_product.html')

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.warning(request, "Product deleted successfully")
    return redirect('admin_dashboard')

@login_required
def buy_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    Sale.objects.create(user=request.user, product=product, quantity=1)
    return redirect('products')  # or a 'thank you' page


@login_required
def my_orders(request):
    orders = Sale.objects.filter(user=request.user).select_related('product')
    return render(request, 'store/my_orders.html', {'orders': orders})

