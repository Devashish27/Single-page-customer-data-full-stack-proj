from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'cust_backend_app_customer';
        