from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer
from .serializers import CustomerSerializer
from cust_backend_data.utils import generate_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Perform additional logic here if needed
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)
            return Response({
                'access': str(access_token),
                'refresh': str(refresh_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCustomerView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SuccessView(APIView):
    def get(self, request):
        # Implement the logic for the success view
        return Response({'message': 'Success!'}, status=status.HTTP_200_OK)
    
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = generate_jwt_token(user)
            return Response({'message': 'User registered successfully', 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PasswordResetView(APIView):
    def post(self, request, *args, **kwargs):
        # Implement logic for resetting passwords
        # This could include sending a password reset email to the user's email address
        # Here, we simply return a success message indicating that the password reset was successful
        return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)

class ProfileUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        # Implement logic for updating user profiles
        # This could include updating user information in the database based on the provided data
        # Here, we simply return a success message indicating that the profile was updated successfully
        return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)

class AccountActivationView(APIView):
    def post(self, request, *args, **kwargs):
        # Implement logic for activating user accounts
        # This could include setting the user's account status to active in the database
        # Here, we simply return a success message indicating that the account was activated successfully
        return Response({'message': 'Account activated successfully'}, status=status.HTTP_200_OK)
