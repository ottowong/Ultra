from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    typeId = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)
    image = models.FileField(upload_to="images/")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to="images/productImages/")
    # def __str__(self):
    #     return self.str(productId)
