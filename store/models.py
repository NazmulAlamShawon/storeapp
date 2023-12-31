from django.db import models

# Create your models here.
class Product (models.Model):
   
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price= models.DecimalField(max_digits=6,decimal_places=2)
    inventories = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

class Collection(models.Model):
  title = models.CharField(max_length=255)
  
class Customer(models.Model):
  MEMBERSHIP_BRONZE = 'B'
  MEMBERSHIP_SILVER = 'S'
  MEMBERSHIP_GOLD = 'G'
  
  MEMBERSHIP_CHOICE = [
      ('MEMBERSHIP_BRONZE','Bronze'),
      ('MEMBERSHIP_SILVER','Sildver'),
      ('MEMBERSHIP_GOLD','Gold')
     ] 
  first_name = models.CharField(max_length=255)  
  last_name = models.CharField(max_length=255)  
  email= models.EmailField(max_length=255) 
  phone = models.CharField(max_length=255)
  birth_date = models.DateField(null=True)
  membership = models.CharField(max_length=17, choices=MEMBERSHIP_CHOICE)
   
  class Order(models.Model):
      PAYMENT_STATUS_PENDING = 'P'
      PAYMENT_STATUS_COMPLETE = 'C'
      PAYMENT_STATUS_FAILD = 'F'
      PAYMENT_STATUS_CHOICES =[
        (PAYMENT_STATUS_PENDING,'P'),
        (PAYMENT_STATUS_COMPLETE,'C'),
        (PAYMENT_STATUS_FAILD,'F'),
      ]
      place_at = models.DateTimeField(auto_now_add=True)
      payment_status= models.CharField(
        max_length=1, choices= PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING
      )
      
  
     
    
    

    