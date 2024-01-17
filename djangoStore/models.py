from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_money_amount = models.IntegerField(default=10000)

    def __str__(self):
        return  f'Профиль {self.user.username}, деньги: {self.user.user_money_amount}'


class Product(models.Model):
    product_name = models.CharField('Name', max_length=50)
    product_discription = models.CharField('Description', max_length=250)
    product_price = models.FloatField('Cost', default=0)
    product_amount = models.FloatField('Amount', default=0)
    product_image = models.ImageField('Logo', upload_to='img/')

    def __str__(self):
        return f'№{self.id} Валюта: {self.product_name} - {self.product_discription}, цена: {self.product_price}, в кол-ве: {self.product_amount} шт.'


class PurchaseProcess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    purchase_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f'Заказ {self.user.username} : {self.product_name}, в кол-ве: {self.amount}, оформлен: {self.purchase_time}'


class Refund(models.Model):
    purchase = models.ForeignKey(PurchaseProcess, on_delete=models.CASCADE)
    request_time = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

    def __str__(self):
        return f'Возврат товара - {self.purchase}, время запроса на возврат - {self.request_time}'

