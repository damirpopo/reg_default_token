from django.contrib import admin
from .models import Cart, Country, Product, User, Order, Author, MyUserManager

admin.site.register(Cart)
admin.site.register(Country)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Author)
