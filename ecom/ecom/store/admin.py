from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)

# Mix profile info and user info in admin panel

class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model    
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name',]
    inlines = [ProfileInline ]
               
# Unregister User
admin.site.unregister(User) 

# Re-register User
admin.site.register(User, UserAdmin)   
