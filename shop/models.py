from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'



class UsersRole(models.Model):
    S_CHOICES = (
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
        ('Diamond', 'Diamond')
    )
    
    designation = models.CharField(max_length=45)
    account = models.CharField(max_length=45)
    billing = models.CharField(max_length=10)
    sale = models.CharField(max_length=100, choices=S_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'UsersRole'
        verbose_name_plural = 'UserRole'


class Types(models.Model):
    CHOICES = (
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
        ('Diamond', 'Diamond')
    )
    type = models.CharField(max_length=7, choices=CHOICES)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Type'


class Items(models.Model):
    gross_weight = models.CharField(max_length=5)
    net_weight = models.CharField(max_length=5)
    labour_wastage = models.CharField(max_length=5)
    purity = models.CharField(max_length=5)
    fine = models.CharField(max_length=5)
    amount = models.CharField(max_length=10) 
    type = models.ForeignKey(Types, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name = 'Item'


class Company(models.Model):
    brand_name = models.CharField(max_length=45)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.brand_name
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'
        

class Vendors(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Vendor'

    
class StockIn(models.Model):
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.items)

    class Meta:
        verbose_name = 'StockIn'
        verbose_name_plural = 'StockIn'


class StockOut(models.Model):
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.items)

    class Meta:
        verbose_name = 'StockOut'
        verbose_name_plural = 'StockOut'


class Reports(models.Model):
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    stockin = models.ForeignKey(StockIn, on_delete=models.CASCADE)
    stockout = models.ForeignKey(StockOut, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.items)

    class Meta:
        verbose_name = 'Report'

class Booking(models.Model):
    price = models.CharField(max_length=10)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.items)
    
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking'