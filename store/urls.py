from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/add/', views.add_product, name='add_product'),
    path('admin-dashboard/delete/<int:id>/', views.delete_product, name='delete_product'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('successful/<int:product_id>/', views.successful, name='successful'),



]
