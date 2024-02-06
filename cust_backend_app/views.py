# from yaml import serialize
from yaml import serialize
from rest_framework import generics 
from .models import Customer
from .serializers import CustomerSerializer
from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.http import HttpResponse

def success_view(request):
    return render(request, 'success.html')

def create_customer(request):
    # if request.method == 'POST':
    #     form = CustomerForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # return redirect('customer-list-create') # redirect to customer list page.
    #         return redirect('success') # redirect to success page.
            
    #     else:
    #         form = CustomerForm()
            
    #     return render(request, 'customer_form.html', {'form': form})
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return HttpResponse("Create Customer View")

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return redirect('success') # redirect to success page
        # return render(request, 'customer_form.html', {'form': CustomerForm()})
    
class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
