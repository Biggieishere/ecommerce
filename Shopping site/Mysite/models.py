from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_photo = models.ImageField(upload_to="Mysite/images",default="")
    
    def __str__(self):
        return f"{self.name}-{self.price}"
    
    
class Cart_Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user} x {self.product.name}'
    
    