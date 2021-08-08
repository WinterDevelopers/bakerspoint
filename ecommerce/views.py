from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


from .forms import CreateUserForm

import json
import datetime

from .models import *

# Create your views here.
def base(request):

    if request.user.is_authenticated:
        user = request.user.email
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_item

    else:
        user = ''
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0}
        cartItem = order['get_cart_item']
    
    template_name = 'ecommerce/base.html'
    print(user)
    context = {'order':order, 'items':items, 'cartItem':cartItem, 'user':user}
    return render(request, template_name, context)


def index(request):

    products = Product.objects.all()[:6]

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_item

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0}
        cartItem = order['get_cart_item']

    template_name  = 'ecommerce/index.html'

    context = {'products':products,'order':order, 'cartItem':cartItem }

    return render(request, template_name, context)

def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print('i have registered')
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been sucssesfully created '+ user)
            return redirect('ecommerce:login')
        else:
            print('cant create user')

    cartItem = 0

    context = {'form':form,'cartItem':cartItem}

    template_name = 'ecommerce/register-page.html'

    return render(request, template_name, context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password = password)
        if user is not None:
            login(request, user)

            customer, created = Customer.objects.get_or_create(user=user)
           
            order, created = Order.objects.get_or_create(customer=customer, complete=False)

            return redirect('ecommerce:index')
        else:
            messages.info(request, 'details not correct')

    cartItem = 0

    context = {'cartItem':cartItem}
    template_name = 'ecommerce/login-page.html'
    return render(request, template_name, context)


def productPage(request, id):

    product = get_object_or_404(Product, id=id)
    qty= product.orderitem_set.all()
    num = sum([okay.quantity for okay in qty])
    other_products = Product.objects.all()[1:6]

    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        

        cartItem = order.get_cart_item

        print('qun:', num)

    else:
        try:
            cart = json.loads(request.COOKIES['cart'])

        except:
            cart={}

        print('cart:', cart)
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0, 'shipping':False}
        cartItem = order['get_cart_item']

        for i in cart:
            try:
                product = Product.objects.get(id=i)
                total = (product.price*cart[i]['quantity'])
                
                cartItem +=  cart[i]['quantity']
                order['get_cart_total'] += total
                order['get_cart_item'] += cart[i]['quantity']

                item = {
                    'product':{
                        'id':product.id,
                        'name':product.name,
                        'price':product.price,
                        'imageURL':product.imageURL
                        },
                    'quantity':cart[i]['quantity'],
                    'get_total':total
                }
                items.append(item)
                if product.digital == False:
                    order.shipping = True
            except:
                pass
    


    template_name = 'ecommerce/product-page.html'

    context = {'product':product, 'items':items, 'cartItem':cartItem, 'other_products':other_products, 'num':num}

    return render(request, template_name, context)

def cartPage(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_item

    else:
        try:
            cart = json.loads(request.COOKIES['cart'])

        except:
            cart={}

        print('cart:', cart)
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0, 'shipping':False}
        cartItem = order['get_cart_item']

        for i in cart:
            try:
                product = Product.objects.get(id=i)
                total = (product.price*cart[i]['quantity'])
                
                cartItem +=  cart[i]['quantity']
                order['get_cart_total'] += total
                order['get_cart_item'] += cart[i]['quantity']

                item = {
                    'product':{
                        'id':product.id,
                        'name':product.name,
                        'price':product.price,
                        'imageURL':product.imageURL
                        },
                    'quantity':cart[i]['quantity'],
                    'get_total':total
                }
                items.append(item)
                if product.digital == False:
                    order.shipping = True
            except:
                pass

    template_name = 'ecommerce/cart-page.html'

    context = {'items':items, 'order':order, 'cartItem':cartItem}

    return render(request, template_name, context)

def paymentPage(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_item

    else:
        items = []
        order = {'get_cart_total':00000, 'get_cart_item':0, 'shipping':True,}
        cartItem = order['get_cart_item']


    template_name = 'ecommerce/payment.html'

    context = {'items':items, 'order':order, 'cartItem':cartItem }

    return render(request, template_name, context)

def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:',action)
    print('productId:', productId)

    customer  = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    
    if action == 'add':
        print('added')

    else:
        pass

    return JsonResponse('item was added...', safe=False)

import datetime

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    print(data)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id


        if total == order.get_cart_total:
            order.complete = True
            print('price was verified')

        else:
            print('price was\'nt veried')

        order.save()
        print('saved')

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
                country = data['shipping']['country']
            )
            print(customer)
        else:
            print('did\'nt save shipping details')
    return JsonResponse('payment was sucssesful...', safe=False)

def notification(request):
    current_customer = request.user.customer
    boss = json.loads(request.body)
    print(boss)

    CompletedTransaction.objects.get_or_create(
        customer = current_customer,
        tracking_id = boss['tracking'],
        message ='this worked'
    )

    return JsonResponse("tracking id was sent", safe=False)


def notification_page(request):

    if request.user.is_authenticated:
        tracking_id  = CompletedTransaction.tracking_id
        messages = CompletedTransaction.message

    else:
        tracking_id = '**********'
        messages = "your are not logged in"

    template_name="ecommerce/notification_page.html"
    context = {"tracking_id":tracking_id, "messages":messages}

    return render(request, template_name, context)