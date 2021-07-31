from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField( default=False)
    image = models.ImageField(default = 'ecommerce/image-4.jpg')
    other_image_1 = models.ImageField(default='chin-chin.jpg')
    other_image_2 = models.ImageField(null=True, blank=True)
    other_image_3 = models.ImageField(null=True, blank=True)
    other_image_4 = models.ImageField(null=True, blank=True)


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


    def __str__(self):
        return self.name

    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_item(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitem ])
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems ])
        return total

    @property
    def shipping(self):
        shipping = False
        orderitem = self.orderitem_set.all()

        for i in orderitem:
            if i.product.digital == False:
                shipping = True

        return shipping

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


    def __str__(self):
        return str(self.order)

    


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country
    

class CompletedTransaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True, blank=True)
    tracking_id = models.CharField(max_length=100, null = True)
    message = models.CharField(max_length=500, null=True)


    @property
    def order(self):
        if Order.complete == True:
            return Order
        else:
            pass

