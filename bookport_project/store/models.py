from django.db import models
from django.contrib.auth.models import User as Users
# Create your models here.
from django.db.models.signals import pre_save


class User(Users):
    pass

c1 = [('english', "english"),('arabic', "arabic"),("maths", "maths")]

class Book(models.Model):

    title = models.CharField(max_length=138)
    author = models.CharField(max_length=64,  blank=True)
    description = models.CharField(max_length=300,  blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=138, choices=c1, default=c1[1])
    # grade = models.CharField(max_length=64,  blank=True)
    image = models.ImageField(blank=True, upload_to='images')
    svg = models.FileField(blank=True, upload_to='images')

    def __str__(self):
        return self.title

class Grade(models.Model):
    # category = models.CharField(max_length=64)
    grade = models.CharField(max_length=64, blank=True)
    books = models.ManyToManyField(Book, related_name="bc")

    def __str__(self):
        return f"{self.grade} grade"


class Quantity(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="quantity_users")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="q_books")
    quantity = models.IntegerField(default=1)

    def checkq(self):
        if self.book.stock == 0 or self.quantity <= 0:
            self.delete()
            return('remove')
        if self.quantity > self.book.stock:
            self.quantity = self.book.stock
            return('solved')
        return('checked')


class Cart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="cart_users")
    items = models.ManyToManyField(Quantity, related_name="items")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def update(self):
        total = 0
        for q in self.items.all():
            x = q.checkq()
            total += q.quantity * q.book.price
        self.total = total



class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_order")
    government = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    address = models.CharField(max_length=64, blank=True)
    ordered = models.BooleanField(default=True)
    paid = models.BooleanField(default=False)





