from django.contrib.auth.models import User
from django.db import models


class Admin(models.Model):
    class Meta:
        db_table = "admin"

    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.login


class Customer(models.Model):
    class Meta:
        db_table = "customer"

    email = models.EmailField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.email


class Category(models.Model):
    class Meta:
        db_table = "category"

    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    class Meta:
        db_table = "product"

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    count = models.IntegerField(null=True)
    photo = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    class Meta:
        db_table = "purchase"

    date = models.DateField(null=True)
    total_price = models.FloatField(null=True)

    def __str__(self):
        return self.total_price


class Cart(models.Model):
    class Meta:
        db_table = "cart"

    purchase = models.ForeignKey(Purchase, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "cart title"


class Cart_content(models.Model):
    class Meta:
        db_table = "cart_content"

    count = models.IntegerField(null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)

    def addProduct(self, product, customer):
        print("lol")


    def __str__(self):
        return self.product.name + str(self.count)


class Customer_phone(models.Model):
    class Meta:
        db_table = "customer_phone"

    address = models.IntegerField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.address


class Customer_address(models.Model):
    class Meta:
        db_table = "customer_address"

    address = models.CharField(max_length=255, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.address
