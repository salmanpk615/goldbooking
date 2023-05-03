from django.contrib import admin

from shop.models import User, UsersRole, Items, Company, Vendors, StockIn, StockOut, Reports, Booking

from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm



# Register your models here.

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["name", "email", "phone"]
    # fieldsets = UserAdmin.fieldsets + (
    #         (None, {'fields': ('name', 'email', 'phone')}),)
 
            #this will allow to change these fields in admin module


class UsersRoleData(admin.ModelAdmin):
    list_display = ("user", "designation", "account", "sale")

class ItemsList(admin.ModelAdmin):
    list_display = ("type", "amount")

class ComapnyData(admin.ModelAdmin):
    list_display = ("brand_name", "phone", "address")

class VendorsData(admin.ModelAdmin):
    list_display = ("name", "address", "email", "items", "company")

class StockInData(admin.ModelAdmin):
    list_display = ("vendor", "items")

class StockOutData(admin.ModelAdmin):
    list_display = ("vendor", "items")

class ReportsData(admin.ModelAdmin):
    list_display = ("user", "vendor", "items", "stockin", "stockout")

class BookingData(admin.ModelAdmin):
    list_display = ("items", "price")


admin.site.register(User, UserAdmin)
admin.site.register(UsersRole, UsersRoleData)
admin.site.register(Items, ItemsList)
admin.site.register(Company, ComapnyData)
admin.site.register(Vendors, VendorsData)
admin.site.register(StockIn, StockInData)
admin.site.register(StockOut, StockOutData)
admin.site.register(Reports, ReportsData)
admin.site.register(Booking, BookingData)
