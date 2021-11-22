from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from shopping_cart.models import Order
from .models import Product, Category
from django.db.models import Q
from .forms import SearchForm, ReviewForm
from django import template
from django.contrib import messages

@login_required
def product_list(request):
    object_list = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    #Unpack the order object to retrieve the order items selected by the user 
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "products/shop/product_list.html", context)
    #return render(request, "products/product_list.html", context)

@login_required
def category(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }  
    return render(request, 'products/shop/categories.html', context)

@login_required
def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    #category = Category.objects.get(id=category_id)
    products = category.product_set.all()#Display these from the template
    categories = Category.objects.all()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/shop/category_detail.html', context)

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.available == True:
        availability = str("Available")
    else:
        availability = str("Not available") 
    front_image = product.album.images.get(name='front') 
    side_image = product.album.images.get(name='side')   
    back_image = product.album.images.get(name='back') 
    seller = product.seller
    seller_products = seller.product_set.all()
    context = {
        'product': product,
        'availability': availability,
        'front_image': front_image,
        'side_image': side_image,
        'back_image': back_image,
        'seller': seller,
        'seller_products': seller_products,
    }
    return render(request, 'products/shop/single-product.html', context)
    #return render(request, 'products/product_detail.html', context)


def search(request):
    form = SearchForm()
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(name__icontains=query) | Q(description__icontains=query)
            results= Product.objects.filter(lookups).distinct()
            context = {
                'results': results,
                'submitbutton': submitbutton,
            }
            return render(request, 'products/shop/search.html', context)
        else:
            return render(request, 'products/shop/search.html')  
    else:
        return render(request, 'products/shop/search.html')

def home(request):
    """Get some of the products to display on the home page"""
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/home.html', context)

#Write a custom template filter here for the product images in the frontend

def wishlist(request, product_id):
    lst = []
    product = Product.objects.filter(pk=product_id)  
    lst.append(product)
    print(lst)
    context = {
        'wishlist': lst,
    }  
    return render(request, 'products/wishlist.html', context)
    


def review(request):#Create the contact form and submit the data to the backend for processing
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                review=form.cleaned_data['review']
            )
            contact.save()
           #Return a message that the review has been recieved
    else:
        form = ContactMessageForm() 
    context = {
        'form': form,
        #'contact': contact,#You may not want to display a contact message
    }           
    return render(request, 'products/review.html', context)
