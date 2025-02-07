from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('items/', views.items, name='items'),
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('purchase/<int:item_id>/', views.purchase_item, name='purchase_item'),
    path('order_success/', views.order_success, name='order_success'),
    path('orders/', views.order_list, name='order_list'),
]