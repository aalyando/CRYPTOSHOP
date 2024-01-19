from djangoStore.models import Product, PurchaseProcess, Refund, Profile
from django.http import HttpResponseRedirect
from djangoStore.forms import FormCreate, ProductForm, ReturnRequestForm, ReturnRequestAdminForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone


def add_to_cart(request, product_id):
    if request.method == 'POST':
        quantity = float(request.POST.get('quantity'))
        product = get_object_or_404(Product, pk=product_id)
        profile = get_object_or_404(Profile, user=request.user)
        if product.product_amount >= quantity and profile.user_money_amount >= quantity * product.product_price:
            purchase = PurchaseProcess.objects.create(user=request.user, product_name=product, amount=quantity)
            product.product_amount -= quantity
            product.save()
            profile.user_money_amount -= quantity * product.product_price
            profile.save()
            return redirect('cart')
        elif product.product_amount < quantity:
            messages.error(request, 'Insufficient quantity of goods in stock')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, 'Not enough money to buy')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def cart(request):
    purchase = PurchaseProcess.objects.all()
    return render(request, 'purchaseprocess.html', {'purchases': purchase})

def product(request):
    return render(request, '')

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {"products_list": products})


def add_product(request):
        if request.method == 'POST':
            form = FormCreate(request.POST)
            if form.is_valid():
                article = form.save(commit=False)
                article.save()
                return redirect('/')
        else:
            form = FormCreate()
        return render(request, 'create.html', {'form': form})


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit.html', {'form': form, 'product': product})


def return_product(request, purchase_id):
    purchase = get_object_or_404(PurchaseProcess, id=purchase_id)
    current_time = timezone.now()
    time_difference = current_time - purchase.purchase_time
    if time_difference.total_seconds() > 180:
        messages.error(request, "The product can only be returned within 3 minutes after purchase.")
        return redirect('cart')

    if request.method == 'POST':
        form = ReturnRequestForm(request.POST)
        if form.is_valid():
            return_request = form.save(commit=False)
            return_request.user = request.user
            return_request.purchase = purchase
            return_request.save()
            messages.success(request, "The return request has been created. Wait for confirmation from the administrator.")
            return redirect('cart')
    else:
        form = ReturnRequestForm()


def view_returns(request):
    return_requests = Refund.objects.all()

    if request.method == 'POST':
        form = ReturnRequestAdminForm(request.POST)
        if form.is_valid():
            return_request = get_object_or_404(Refund, id=form.cleaned_data['return_request_id'])
            if form.cleaned_data['approved']:
                purchase = return_request.purchase
                purchase.product_name.product_amount += float(purchase.amount)
                purchase.product_name.save()
                user = purchase.user
                user.profile.user_money_amount += float(purchase.amount) * purchase.product_name.product_price
                user.profile.save()
                purchase.delete()
            elif form.cleaned_data['rejected']:
                return_request.delete()

            messages.success(request, "Refund processed successfully.")
            return redirect('view_returns')
    else:
        form = ReturnRequestAdminForm()

    return render(request, 'all_returns.html', {'return_requests': return_requests, 'form': form})

