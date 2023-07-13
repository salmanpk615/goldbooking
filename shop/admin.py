from django.contrib import admin

from shop.models import User, UsersRole, Items, Company, Vendors, StockIn, StockOut, Reports, Booking, Types

from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm


# Register your models here.

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["email", "username"]
    # fieldsets = UserAdmin.fieldsets + ((None, {"fields": ["email"]}),)


class UsersRoleData(admin.ModelAdmin):
    list_display = ("user", "designation", "account", "sale")


class ItemsList(admin.ModelAdmin):
    list_display = ("name", "type", "amount")


class TypeList(admin.ModelAdmin):
    list_display = ("type",)


class ComapnyData(admin.ModelAdmin):
    list_display = ("brand_name", "phone", "address")


class VendorsData(admin.ModelAdmin):
    list_display = ("name", "address", "email", "company")


class StockInData(admin.ModelAdmin):
    list_display = ("vendor", "items")


class StockOutData(admin.ModelAdmin):
    list_display = ("vendor", "items")


class ReportsData(admin.ModelAdmin):
    list_display = ("vendor", "items", "stockin", "stockout")


class BookingData(admin.ModelAdmin):
    list_display = ("items", "price")


admin.site.register(User, UserAdmin)
admin.site.register(UsersRole, UsersRoleData)
admin.site.register(Items, ItemsList)
admin.site.register(Types, TypeList)
admin.site.register(Company, ComapnyData)
admin.site.register(Vendors, VendorsData)
admin.site.register(StockIn, StockInData)
admin.site.register(StockOut, StockOutData)
admin.site.register(Reports, ReportsData)
admin.site.register(Booking, BookingData)
