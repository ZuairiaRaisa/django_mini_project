from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, ContactMessage, Order
from .forms import ContactForm, OrderForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def items(request):
    items = Item.objects.all()
    return render(request, 'items.html', {'items': items})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def purchase_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.item = item
            order.total_price = item.price * order.quantity
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'purchase.html', {'item': item, 'form': form})

def order_success(request):
    return render(request, 'order_success.html')

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})