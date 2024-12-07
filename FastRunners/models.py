from django.db import models

# Create your models here.
#This defines the database schema using python classes
from django.db import models


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Car Model
class Car(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='cars', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Order Model
class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=(
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ), default='Pending')

    def __str__(self):
        return f"Order {self.id} - {self.car.name}"

