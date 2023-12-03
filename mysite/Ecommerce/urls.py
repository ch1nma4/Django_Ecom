from django.urls import path 
from Ecommerce import views

app_name = 'Ecommerce'

urlpatterns = [

    path('store/' , views.store , name='store'),
    path('cart/' , views.cart , name='cart'),
    path('checkout/' , views.checkout , name='checkout'),
    
]

    
    

