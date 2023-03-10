from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('product/<str:product_id>/', views.product_update, name="product_update"),
    path('create_product/', views.create_product, name="create_product"),
    path('product_delete/<str:product_id>/', views.product_delete, name="product_delete")
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)