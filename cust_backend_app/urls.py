from django.urls import path
from .views import CustomerListCreateView, CustomerDetailView, CreateCustomerView, SuccessView, CustomTokenObtainPairView, UserRegistrationView, PasswordResetView, ProfileUpdateView, AccountActivationView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('create-customer/', CreateCustomerView.as_view(), name='create-customer'),
    path('success/', SuccessView.as_view(), name='success-page'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', UserRegistrationView.as_view(), name='user_registration'),
    path('reset-password/', PasswordResetView.as_view(), name='password_reset'),
    path('update-profile/', ProfileUpdateView.as_view(), name='profile_update'),
    path('activate-account/', AccountActivationView.as_view(), name='account_activation'),
]
