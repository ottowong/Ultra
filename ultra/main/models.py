from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    address3 = models.CharField(max_length=200)
    stateCounty = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)
    admin = models.BooleanField(default=0)
    def __str__(self):
        return self.email

class DeliveryAddress(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    address3 = models.CharField(max_length=200)
    stateCounty = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)

class Order(models.Model):
    userId = models.ForeignKey(User, on_delete=models.PROTECT)
    deliveryAddressId = models.ForeignKey(DeliveryAddress, on_delete=models.PROTECT)
    status = models.IntegerField(default=0)

class Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    typeId = models.ForeignKey(Type, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)
    image = models.FileField(upload_to="images/")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.PROTECT)
    productId = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

class ProductImage(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.FileField(upload_to="images/productImages/")
    # def __str__(self):
    #     return self.str(productId)
