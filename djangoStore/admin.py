from django.contrib import admin
from .models import Profile, Product, PurchaseProcess, Refund

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(PurchaseProcess)
admin.site.register(Refund)
