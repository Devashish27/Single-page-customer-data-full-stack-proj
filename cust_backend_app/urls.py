from django.urls import path
from .views import CustomerListCreateView, CustomerDetailView, create_customer, success_view

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('create/', create_customer, name='create-customer'),
    path('success/', success_view, name='success-page'),
]
