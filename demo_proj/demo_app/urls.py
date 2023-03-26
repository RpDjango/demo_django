from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('product/<str:product_id>/', views.product_update, name="product_update"),
    path('create_product/', views.create_product, name="create_product"),
    path('product_delete/<str:product_id>/', views.product_delete, name="product_delete"),
    path('login/', views.user_login, name="user_login"),
    path('registration/', views.registration, name="registration"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"), 
    path('cart_detail/', views.cart_detail, name="cart_detail"),  

]  