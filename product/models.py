from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from datetime import datetime,date
import uuid
import os

# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_retailer = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100,default="",blank=True)
    last_name = models.CharField(max_length=100,blank=True,default = "")
    email = models.EmailField(max_length=265)
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    def __str__(self):
        return self.username


class Product(models.Model):
    
    boolChoice = (
        ("mb","Mobile & Accesary"),
        ("fb","Food and Bevarages"),
        ("cl","Clothing"),
        ("el","Electronics"),
    )
    boolcChoice = (
        ("us","America"),
        ("in","India"),
        ("it","Italy"),
        ("brt","Britain"),
        ("rs","Russia"),
    )

    username = models.ForeignKey(User , on_delete=models.CASCADE)
    slug = models.SlugField(default="")
    first_name = models.CharField(max_length=264, default="",blank=True)
    last_name = models.CharField(max_length=264,default="",blank=True)
    comapany_name = models.CharField(max_length=264,default="",blank=True)
    product_name = models.CharField(max_length=264,default="",blank=True)
    manufacturer_name = models.CharField(max_length=264,default="",blank=True)
    product_number = models.CharField(max_length=100,unique=True)
    category = models.CharField(max_length=100,choices=boolChoice,null=True)
    Images = models.TextField(null=True,default="H&Y.png")
    landline_no = models.CharField(max_length=100,default="",blank=True)
    mobile_no = models.CharField(max_length=100,blank=True,default="")
    address1 = models.CharField(max_length=400,blank=True,default="")
    address2 = models.CharField(max_length=400,default="",blank=True)
    state = models.CharField(max_length=100,default="",blank=True)
    postcode = models.CharField(max_length=100,default="",blank=True)
    city = models.CharField(max_length=200,default="",blank=True)
    country = models.CharField(max_length=264,choices=boolcChoice,null=True)

    def __str__(self):
        return self.product_name
    





    

    