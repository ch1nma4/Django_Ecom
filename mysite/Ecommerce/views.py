from django.shortcuts import render

# Create your views here.

def store(request):
    context = { 

    }

    return render(request , 'Ecommerce/Store.html',context)

def cart(request):
    context = {

    }

    return render(request , 'Ecommerce/Cart.html',context)

def checkout(request):
    context = {

    }

    return render(request , 'Ecommerce/Checkout.html',context)