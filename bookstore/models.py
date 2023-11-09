from django.db import models
from django.contrib.auth.models import User

class Authors(models.Model):
    
    firstname = models.CharField(max_length=100)
    lastname=models.CharField(max_length=150)
    description=models.CharField(max_length=400,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    

    
class Book(models.Model):
    title=models.CharField(max_length=255)
    author = models.ManyToManyField(Authors,related_name='author')
    price=models.FloatField(max_length=10)
    description=models.CharField(max_length=400,blank=True)
    picture =models.ImageField(upload_to='uploads/')
    e_version=models.FileField(upload_to='documents/', max_length=150,blank=True)
   
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.title 

# class Authors(models.Model):
#     books=models.ForeignKey(Book, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name    

class Category(models.Model):
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
    
class Customer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=250)
    email=models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
   
    STATUS = (
        
        ('Done','Done'), 
        ('New', 'New'),
        ('In Progress','In Progress')
       
    )
    order_date=models.DateField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    status = models.CharField(max_length = 100, choices = STATUS, default="New")

    def __str__(self) -> str:
        return self.status


class Category_book(models.Model):
    book_id=models.ForeignKey(Book, on_delete=models.CASCADE)   
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE) 
    
class Likes(models.Model):
    book_id=models.ForeignKey(Book, on_delete=models.CASCADE)  
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateField(auto_now=True)
