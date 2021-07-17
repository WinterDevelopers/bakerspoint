from django.urls import path

from .views import index, productPage, cartPage, paymentPage, updateItem, processOrder, notification, registerPage, loginPage


app_name = 'ecommerce'

urlpatterns = [
    path('/', index, name ='index'),
    path('registration/', registerPage, name= 'registration'),
    path('login/', loginPage, name='login'),
    path('cart-page/', cartPage, name = 'cart-page'),
    path('payment-page/', paymentPage, name= 'payment-page'),
    path('update-item/', updateItem, name = 'update-item'),
    path('process-order/', processOrder, name = 'process-order'),
    path('notification', notification, name = 'notification'),
    path('<slug:id>/', productPage, name ='product-page' )
    
    

]