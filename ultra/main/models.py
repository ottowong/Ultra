from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Colour(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    typeId = models.ForeignKey(Type, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.FileField(upload_to="images/")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return (self.name +" "+ str(self.typeId))

class ProductColour(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    colourId = models.ForeignKey(Colour, on_delete=models.CASCADE)
    def __str__(self):
        return (str(self.colourId) + " " + str(self.productId))

class ProductImage(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to="images/productImages/")
    def __str__(self):
        return str(self.productId)

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
    userId = models.ForeignKey(User, on_delete=models.PROTECT)
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
    deliveryAddressId = models.ForeignKey(DeliveryAddress, on_delete=models.PROTECT)
    status = models.IntegerField(default=0)

class OrderItem(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.PROTECT)
    productId = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)